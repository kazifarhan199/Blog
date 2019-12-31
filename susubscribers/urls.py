from django.urls import path

from .views import subscribe_add

urlpatterns = [
    path('', subscribe_add, name='subscribe'),
]