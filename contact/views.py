from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializers
from rest_framework.decorators import api_view

@api_view(['POST'])
def post_contact_api_views(request, format=None):
    if request.method == "POST":
        serializers = ContactSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errers, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_contact_api_views(request, format=None):
      if request.method == "GET":
        contacts=Contact.objects.all()
        serializers = ContactSerializers(contacts, many=True)
        return Response(serializers.data)


