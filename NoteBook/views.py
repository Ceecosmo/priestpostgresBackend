from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Notebook
from .serializers import NotebookSerializers
from rest_framework.decorators import api_view

@api_view(['POST'])
def post_NoteBook_api_views(request, format=None):
    if request.method == "POST":
        serializers = NotebookSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errers, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_NoteBook_api_views(request, format=None):
      if request.method == "GET":
        NoteBooks=Notebook.objects.all()
        serializers = NotebookSerializers(NoteBooks, many=True)
        return Response(serializers.data)


