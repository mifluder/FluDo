from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

from app.models.list import ListItem as ListItemModel
from app.models.list import TodoList as TodoListModel
from app.schemas.list import EmptyTodoList, Title, TodoList

router = APIRouter()


@router.post("/{title}", response_model=EmptyTodoList)
async def create_list(title: Title):
    todo_list = await TodoListModel.create(title=title)
    return todo_list


@router.get("/{list_id}/items", response_model=TodoList)
async def get_list_with_all_items(list_id: int):
    todo_list = await get_list_from_db(list_id)
    await todo_list.fetch_related("items")
    return todo_list


@router.put("/{list_id}/{title}", response_model=EmptyTodoList)
async def update_list(list_id: int, title: Title):
    todo_list = await get_list_from_db(list_id)
    todo_list.update_from_dict({"title": title})
    return todo_list


@router.delete("/{list_id}")
async def delete_list(list_id: int) -> None:
    todo_list = await get_list_from_db(list_id)
    await todo_list.delete()
    return


async def get_list_from_db(list_id: int) -> TodoListModel:
    todo_list = await TodoListModel.get_or_none(id=list_id)
    if not todo_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"List {list_id} not found."
        )
    return todo_list
