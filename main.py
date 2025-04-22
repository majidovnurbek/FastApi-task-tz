from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers.auth import router as auth_router
from routers import auth, course, lesson, comment  # import routers

from database import  engine
from fastapi.openapi.models import OAuthFlows, OAuthFlowAuthorizationCode
app = FastAPI()
from models import user

app.include_router(auth.router)  # Auth router
app.include_router(course.router)  # Course router
app.include_router(lesson.router)  # Lesson router
app.include_router(comment.router)  # Comment router

@app.get("/")
def read_root():
    return {"message": "Online Course Platform API"}

app = FastAPI()

user.Base.metadata.create_all(bind=engine)


# OAuth2PasswordBearer token URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")



app.include_router(auth_router)

# Swaggerda tokenni authorize qilish uchun
@app.get("/openapi.json")
async def get_open_api():
    return app.openapi()
