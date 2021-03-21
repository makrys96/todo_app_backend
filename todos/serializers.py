from rest_framework import serializers

from todos.models import TodoList, Todo

class TodoListSerializer(serializers.ModelSerializer):
    number_of_tasks = serializers.SerializerMethodField()
    number_of_done_tasks = serializers.SerializerMethodField()
    class Meta:
        model = TodoList
        fields = '__all__'

    def get_number_of_tasks(self, instance):
        return instance.get_number_of_tasks()
    def get_number_of_done_tasks(self, instance):
        return instance.get_number_of_done_tasks()

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
