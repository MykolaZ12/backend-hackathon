from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.order.endpoinds import order
from app.user.endpoints import login, user
from config import settings


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(login.router, prefix=settings.API_V1_STR + "/user", tags=["login"])
app.include_router(user.router, prefix=settings.API_V1_STR + "/user", tags=["user"])
app.include_router(order.router, prefix=settings.API_V1_STR + "/order", tags=["order"])
