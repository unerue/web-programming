from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

class WelcomeView(APIView):
    def get(self, request):
        return Response({"message": "Hello World"})

class TodoListCreateView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({"todos": serializer.data})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Todo added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailView(APIView):
    def get(self, request, todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
            serializer = TodoSerializer(todo)
            return Response({"todo": serializer.data})
        except Todo.DoesNotExist:
            return Response({"message": "Todo with supplied ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return Response({"message": "Todo with supplied ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Todo updated successfully."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return Response({"message": "Todo deleted successfully."})
        except Todo.DoesNotExist:
            return Response({"message": "Todo with supplied ID doesn't exist."}, status=status.HTTP_404_NOT_FOUND)

class TodoDeleteAllView(APIView):
    def delete(self, request):
        Todo.objects.all().delete()
        return Response({"message": "Todos deleted successfully."})