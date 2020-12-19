from fastapi import FastAPI

from app.order.endpoinds import order
from app.user.endpoints import login, user
from config import settings


app = FastAPI()


app.include_router(login.router, prefix=settings.API_V1_STR + "/user", tags=["login"])
app.include_router(user.router, prefix=settings.API_V1_STR + "/user", tags=["user"])
app.include_router(order.router, prefix=settings.API_V1_STR + "/order", tags=["order"])
