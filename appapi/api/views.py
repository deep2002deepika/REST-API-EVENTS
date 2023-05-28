from django.shortcuts import render
from rest_framework import viewsets
from api.models import app
from api.serializers import AppSerializer

# Create your views here.
class AppViewset(viewsets.ModelViewSet):
    queryset=app.objects.all()
    serializer_class=AppSerializer
