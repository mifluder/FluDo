from tortoise import fields
from tortoise.models import Model

# class UserManagedLists(Model):
# id = fields.IntField(pk=True)
# user_id =


class TodoList(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    title = fields.CharField(max_length=100)


class ListItem(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    # updated_by = ??? would be nice if multiple users use this
    # maybe use update model or something like that.
    list: fields.ForeignKeyRelation[TodoList] = fields.ForeignKeyField(
        "models.TodoList", related_name="items"
    )
    title = fields.CharField(max_length=100)
    description = fields.TextField(default="")
    done = fields.BooleanField(default=False)

    def __str__(self):
        return f"ListItem of a TodoList.list_id={self.list_id}"
