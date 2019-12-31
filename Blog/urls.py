from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from .views import about

urlpatterns = [
    path('', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('susubscribers/', include('susubscribers.urls')),
    path('accounts/', include('accounts.urls')),
    path('comments/', include('comments.urls')),
    path('about/', about, name='about'),

    re_path(r'media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
