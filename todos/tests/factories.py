import factory.fuzzy

from todos.models import TodoList, Todo

class TodoListFactory(factory.DjangoModelFactory):
    class Meta:
        model = TodoLists

    name = factory.fuzzy.FuzzyText()
    description = factory.fuzzy.FuzzyText()

class TodoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Todo

    name = factory.fuzzy.FuzzyText()
    done = False
    todo_list = factory.SubFactory(TodoListFactory)