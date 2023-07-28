from django.urls import path
from .views import GetApis

urlpatterns = [
    path('GetApis',GetApis.as_view())
]