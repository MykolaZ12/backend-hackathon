from app.base.crud import CRUDBase
from app.order import schemas
from app.order.models import Order


class OrderCRUD(CRUDBase[Order, schemas.OrderCreate, schemas.OrderUpdate]):
    pass