from typing import List

from sqlalchemy.orm import Session

from app.base.crud import CRUDBase
from app.order import schemas
from app.order.models import Order


class OrderCRUD(CRUDBase[Order, schemas.OrderCreate, schemas.OrderUpdate]):
    def agree_order(self, db: Session, user_id: int, order_obj: Order):
        order_obj.volunteer = user_id
        order_obj.status = "agree"
        db.add(order_obj)
        db.commit()
        db.refresh(order_obj)

    def get_multi_by_user(self, db: Session, user_id: int):
        orders = db.query(self.model).filter_by(user_id=user_id).all()
        return orders

    def get_only_open(self, db: Session, skip: int = 0, limit: int = 100) -> List[Order]:
        return db.query(self.model).filter_by(status="open").offset(skip).limit(limit).all()


order_crud = OrderCRUD(Order)
