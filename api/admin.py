from django.contrib import admin
from .models.user import User
from .models.todo import ToDo

admin.site.register(User)
admin.site.register(ToDo)

