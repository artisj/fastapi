#import uvicorn

from db import db
from app.deps import authorize

from fastapi import APIRouter, HTTPException, Depends
from . import schemas
from bson.json_util import dumps

tags_metadata = [{'name': 'Blog Methods', 'description': 'Methods for blog'}]

swag_responses = {400: {"detail": "Data received invalid"}}

blog_router = APIRouter()

# {'_id': ObjectId('630beb212e81f6c2f5be2e0b'),
#  'body': 'huge body',
#  'title': 'twenty eighth'}


# update
@blog_router.put('/blog/{id}', tags=['Blog Methods'], responses=swag_responses)
def update_post(id: str, post: schemas.Blog):
    message = db.update_entry('blog', id, post.dict())

    if (message):
        raise HTTPException(status_code=message['status'],
                            detail=message['error'])

    return {'message': 'your post updated'}


# delete
@blog_router.delete('/blog/{id}', tags=['Blog Methods'])
async def delete_post(id: str):
    db.delete('blog', id)
    return {'message': f'Item {id} deleted'}


# add
@blog_router.post("/blog", tags=['Blog Methods'])
async def create(request: schemas.Blog, id: str = Depends(authorize)):
    print(id)
    print(request)
    if schemas.Blog:
        user_blog = {}
        user_blog.update(request.dict())
        user_blog['id'] = id
        print(user_blog)
        db.add_entry('blog', user_blog)

    return user_blog


# read
@blog_router.get('/blog', tags=['Blog Methods'])
async def get_blogs(id: str = Depends(authorize)):

    blog_dict = list(db.list_items('blog', id))
    json_data = dumps(blog_dict)
    return json_data
