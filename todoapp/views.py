from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import  viewsets

class TodoView(viewsets.ModelViewSet):
	serializer_class = TaskSerializer
	queryset = Task.objects.all().order_by('-id')
