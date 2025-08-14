from rest_framework import serializers
from api.models.todo import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
