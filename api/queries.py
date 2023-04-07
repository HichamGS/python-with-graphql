from .models import Post
from api import db
from ariadne import convert_kwargs_to_snake_case
from datetime import date

def listPosts_resolver(obj, info):
    try: 
        posts = [post.to_dict() for post in Post.query.all()]
        print(posts)
        payload  = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found !"]
        }
    return payload

@convert_kwargs_to_snake_case
def createPost_resolver(obj, info, title, description):
    try:
        today = date.today()
        post = Post(
            title=title, 
            description=description, 
            created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(post)
        db.session.commit()
        payload = {
            "success":True,
            "post": post.to_dict()
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": ["Incorrect data provided"]
        }
    return payload

@convert_kwargs_to_snake_case
def updatePost_resolver(obj, info, id, title, description):
    try:
        post = Post.query.get(id)
        if post:
            post.title = title
            post.description = description
        db.session.add(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def deletePost_resolver(obj, info, id):
    try:
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload