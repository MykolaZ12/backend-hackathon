from sqlalchemy.orm import Session

from app.base.crud import CRUDBase
from app.order import schemas
from app.order.models import Order


class OrderCRUD(CRUDBase[Order, schemas.OrderCreate, schemas.OrderUpdate]):
    def agree_order(self, db: Session, user_id: int, order_obj: Order):
        order_obj.volunteer = user_id
        db.add(order_obj)
        db.commit()
        db.refresh(order_obj)


order_crud = OrderCRUD(Order)
