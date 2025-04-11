from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World!!"}


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         database="fastapi",
#         user="postgres",
#         password="root",
#         cursor_factory=psycopg2.extras.RealDictCursor,
#     )
#     cursor = conn.cursor()
#     print("Database connection successful!!")
# except Exception as e:
#     print(f"Connection to database failed: {e}")
#     exit


# @app.get("/posts")
# def get_posts():
#     cursor.execute(""" SELECT * FROM posts """)
#     posts = cursor.fetchall()
#     return {"data": posts}


# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute(""" SELECT * FROM posts WHERE id=%s""", (str(id),))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} not found.",
#         )

#     return {"data": post}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
#     cursor.execute(
#         """ INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#         (post.title, post.content, post.published),
#     )
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}


# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute(
#         """ UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""",
#         (post.title, post.content, post.published, str(id)),
#     )
#     updated_post = cursor.fetchone()
#     if not updated_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} not found.",
#         )

#     conn.commit()
#     return {"data": updated_post}


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute(""" DELETE FROM posts WHERE id=%s RETURNING *""", (str(id),))
#     deleted_post = cursor.fetchone()
#     if not deleted_post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Post with id: {id} not found.",
#         )

#     conn.commit()
#     # return Response(status_code=status.HTTP_204_NO_CONTENT)
