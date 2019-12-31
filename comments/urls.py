from django.urls import path
from .views import comment_add

urlpatterns = [
    path('add/', comment_add, name='comment_add')
]