from typing import  Optional, List

from .models import ItemRead, ItemCreate, Item



def get(*, db_session, document_id: int) -> Optional[Item]:
    """Returns a document based on the given item id."""
    return db_session.query(ItemRead).filter(ItemRead.id == document_id).one_or_none()


def get_all(*, db_session) -> List[Optional[ItemRead]]:
    """Returns all items."""
    return db_session.query(ItemRead)



def create(*, db_session, item_in: ItemCreate) -> Item:
    """Creates a new document."""
    project = None

    item = Item(**item_in.dict())

    db_session.add(item)
    db_session.commit()
    return item