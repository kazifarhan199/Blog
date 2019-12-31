from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CommentForm
from .models import Comment

def comment_add(request):
    if request.method == 'GET':
        if request.META.get('HTTP_REFERER'):
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(reverse('post'))

    elif request.method == 'POST':
        prevous = request.POST.get('previous')
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Comment has been added')
        else:
            messages.add_message(request, messages.ERROR, form.errors)

        if prevous:
            return redirect(prevous)
        elif request.META.get('HTTP_REFERER'):
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect(reverse('post'))
