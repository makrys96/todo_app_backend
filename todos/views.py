from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from todos.models import TodoList, Todo
from todos.serializers import TodoListSerializer, TodoSerializer

class TodoListViewSet(ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_fields = ('todo_list', 'done')

