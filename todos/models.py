from django.db import models

class TodoList(models.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self): #zwraca opisową reprezentację obiektu
        return self.name

    def get_number_of_tasks1(self): #wyliczanie liczby zadań powiazanych
        l = Todo.objects.filter(todo_list=self)
        return len(l) #pobieranie obiektów z bazy danych (Pobiera bazę danych)

    def get_number_of_tasks2(self):
        return Todo.objects.filter(todo_list=self).count();#oddelegowanie sortowania do bazy danych

    def get_number_of_tasks(self):#menadżer, który reprezentuje obiekty todo powiązanie z todoList
        x = self.todos.all() #obiekty qyeryset są leniwe, zapytanie zostanie wykonane
        y = x.filter(id = 1) #kiedy będzie to konieczne
        print(y) #dopiero w tym miejscu zostanie wysłane zapytanie do bazy danych
        return self.todos.all().count() #oddelegowane do bazy danych

    def get_number_of_done_tasks(self): #pobieranie poprawnych wyników
        return self.todos.filter(done=True).count()

class Todo(models.Model):
    name = models.CharField(max_length=128)
    done = models.BooleanField(default=False)              #self.todos#related_name django doda automatycznie pole. możemy odwołaś cie do wszystkich obiektów todos
    todo_list = models.ForeignKey('todos.TodoList', on_delete=models.CASCADE, related_name='todos')#co się stanie po usunięciu todolis

    def __str__(self): #konkatenacja napisów, możemy sobie zabisać itrał f'String'
        return f'{self.name} [{self.todo_list.name}]'#z f zostanie wstawiona wartość name z Todo, a z 2 name z TodoList
