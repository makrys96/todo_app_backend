from rest_framework.routers import DefaultRouter
from django.urls import path, include
from todos.views import TodoListViewSet, TodoViewSet

router = DefaultRouter()
router.register('todo-lists', TodoListViewSet)
router.register('todos', TodoViewSet)

urlpatterns = router.urls