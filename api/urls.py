from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, ToDoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'todos', ToDoViewSet, basename='todo')

urlpatterns = router.urls
