import uuid
from django.db import models
from .user import User

class ToDo(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
