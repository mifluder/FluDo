from typing import Any

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.models.list import ListItem as ListItemModel
from app.schemas.list import ListItem, ListItemCreate, ListItemUpdate

router = APIRouter()


@router.get("/{item_id}", response_model=ListItem)
async def get_item_by_id(item_id: int) -> Any:
    item = await get_item_from_db(item_id)
    return item


@router.post("/{list_id}", response_model=ListItem)
async def create_list_item(list_id: int, data: ListItemCreate) -> Any:
    item = await ListItemModel.create(list_id=list_id, **data.model_dump(exclude_defaults=True))
    return item


@router.put("/{item_id}", response_model=ListItem)
async def update_list_item(item_id: int, data: ListItemUpdate) -> Any:
    item = await get_item_from_db(item_id)
    item.update_from_dict(data.model_dump(exclude_defaults=True))
    return item


@router.delete("/{item_id}")
async def delete_list_item(item_id: int) -> None:
    item = await get_item_from_db(item_id)
    await item.delete()
    return


async def get_item_from_db(item_id: int) -> ListItemModel:
    item = await ListItemModel.get_or_none(id=item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"item with id {item_id} not found."
        )
    return item
