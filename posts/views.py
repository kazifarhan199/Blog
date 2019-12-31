from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from comments.models import Comment
from .models import Post

class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        context = super().get_queryset()
        context = context.filter(published=True)
        search = self.request.GET.get('search')
        if search:
            context = context.filter(
                Q(title__icontains=search)
                | Q(body__icontains=search)
            )
        return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        if self.request.GET.get('search'):
            context['search'] = self.request.GET.get('search')
        return context

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['comments'] = Comment.objects.filter(post=context['object']).order_by('-id')
        return context
