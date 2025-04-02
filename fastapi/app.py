from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid

app=FastAPI()

#creamos un arrary
posts=[]

class Post(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    create_at: datetime = datetime.now()
    publised_at: Optional[datetime]
    publised: bool = False


#http://127.0.0.1:8000/
@app.get('/')
def read_root():
    return{"welcome":"bienvenidos a mi Rest api"}

#http://127.0.0.1:8000/posts
@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    print(post_id)
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail= "post no econtrado") 

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        print(index)
        print(post)
        if post["id"] == post_id:
            posts.pop(index)
            return{"message": "post eliminado"}    
    raise HTTPException(status_code=404, detail= "post no econtrado")

@app.put('/posts/{post_id}')
def update_post(post_id:str, updatedPost:Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = updatedPost.title
            posts[index]["content"] = updatedPost.content
            posts[index]["author"] = updatedPost.author
            return{"message": "post modificado"} 
    raise HTTPException(status_code=404, detail= "post no econtrado")
        
            
            




