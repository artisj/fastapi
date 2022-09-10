import uvicorn
from blog import blog
from user import user
from fastapi import FastAPI

tags_metadata = [{'name': 'Blog Methods', 'description': 'Methods for blog'},{
                 'name': 'User Methods', 'description': 'Methods for users'
}]

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(blog.blog_router)
app.include_router(user.user_router)



@app.get('/')
async def home():
  return 'Home'



  
uvicorn.run(app,host="0.0.0.0",port=8080)