from typing import  Optional, List

from .models import ProductRead, ProductCreate, Product



def get(*, db_session, item_id: int) -> Optional[Product]:
    """Returns a item based on the given item id."""
    return db_session.query(Product).filter(Product.id == item_id).one_or_none()


def get_all(*, db_session) -> List[Optional[Product]]:
    """Returns all items."""
    return db_session.query(Product)



def create(*, db_session, item_in: ProductCreate) -> Product:
    """Creates a new item."""
    project = None

    item = Product(**item_in.dict())

    db_session.add(item)
    db_session.commit()
    return item