import pytest
from rest_framework import status

from todos.tests.factories import TodoListFactory, TodoFactory

@pytest.mark.django_db
def test_todo_list(client):
    TodoListFactory()
    TodoListFactory()

    response = client.get('api/v1/todos/todo-lists/')
    print(response.data)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1



