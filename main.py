from fastapi import FastAPI
from app.order.endpoinds import order
from app.user.endpoints import login, user

app = FastAPI()


app.include_router(login.router, prefix="/login", tags=["login"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(order.router, prefix="/order", tags=["order"])
