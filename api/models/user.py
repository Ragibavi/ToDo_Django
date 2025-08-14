import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
