import pytest
import todos.models import TodoList, Todo

from todos.tests.factories import TodoListFactory, TodoFactory
@pytest.mark.django_db

def test_todo_list_str():
    todo_list = TodoList(name='Lista 1')
    assert str(todo_list == 'Lista 1') #jeśli true to przechodzi dalej, jeżeli nie, rzuca nam wyjatek

@pytest.mark.django_db
def test_todo_list_number_of_tasks():
    l1 = TodoListFactory()
    l2 = TodoListFactory()
    t1 = TodoListFactory(todo_list=l1)
    t2 = TodoListFactory(todo_list=l1)
    t3 = TodoListFactory(todo_list=l2)
    assert  l1.get_number_of_task() == 2
    assert l2.get_number_of_task() == 1

@pytest.mark.django_db
def test_todo_list_number_of_done_tasks():
    l1 = TodoList.objects.create(name='Lista 1', description='')
    l2 = TodoList.objects.create(name='Lista 2', description='')
    t1 = Todo.objects.create(name='Zadanie 1',done=True, todo_list=l1)
    t2 = Todo.objects.create(name='Zadanie 2', done=True, todo_list=l1)
    t3 = Todo.objects.create(name='Zadanie 3', done=True, todo_list=l2)
    assert  l1.get_number_of_done_task() == 2
    assert l2.get_number_of_done_task() == 1