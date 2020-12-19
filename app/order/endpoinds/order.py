from typing import List, Optional, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.order import services, schemas
from app.user import permission
from app.user.models import User
from db.db import get_db

router = APIRouter()


@router.get("/{id}", response_model=schemas.OrderInResponse)
def get_order(*, id: int, db: Session = Depends(get_db)):
    order = services.order_crud.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.get("/", response_model=List[schemas.OrderInResponse])
def get_list_orders(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    orders = services.order_crud.get_multi(db=db, skip=skip, limit=limit)
    if not orders:
        raise HTTPException(status_code=404, detail="Orders not found")
    return orders


@router.post("/", response_model=schemas.OrderCreate)
def create_order(
        *,
        db: Session = Depends(get_db),
        schema: schemas.OrderCreate,
        current_user: User = Depends(permission.get_current_active_user),
) -> Any:
    order_in_db = schemas.OrderInDB(**schema.dict(), user_id=current_user.id)
    order = services.order_crud.create(db=db, schema=order_in_db)
    return order


@router.put("/{id}", response_model=schemas.OrderUpdate)
def update_order(
        *,
        db: Session = Depends(get_db),
        id: int,
        schema: schemas.OrderUpdate,
        current_user: User = Depends(permission.get_current_active_user),
):
    order = services.order_crud.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not current_user.is_superuser and (order.user_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    order = services.order_crud.update(db=db, db_obj=order, schema=schema)
    return order


@router.delete("/{id}", response_model=schemas.OrderInResponse)
async def delete_order(
        *,
        db: Session = Depends(get_db),
        id: int,
        current_user: User = Depends(permission.get_current_active_user),
):
    order = services.order_crud.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not current_user.is_superuser and (order.user_id != current_user.id):
        raise HTTPException(status_code=404, detail="Not enough permissions")
    order = services.order_crud.remove(db=db, id=id)
    return order
