from django.urls import path, include
from .views import profile, AccountEdit, AccountDelete

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', profile, name='profile'),
    path('account/delete/', AccountDelete.as_view(), name='account_delete'),
    path('profile/edit/', AccountEdit.as_view(), name='account_edit'),
]