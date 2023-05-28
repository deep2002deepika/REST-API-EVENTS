from django.contrib import admin
from django.urls import path,include
from api.views import AppViewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'app', AppViewset)

urlpatterns = [
    path('',include(router.urls))
]