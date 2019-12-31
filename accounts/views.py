from django.shortcuts import render, reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import get_user_model
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin

User = get_user_model()

def profile(request):
    return render(request, 'accounts/profile.html')

class AccountEdit(LoginRequiredMixin, UpdateView):
	model = User
	success_url = '/accounts/login'
	fields = ['email', 'username']
	template_name = 'accounts/edit.html'

	def get_object(self, queryset=None):
		user = self.request.user 
		return user

class AccountDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = '/accounts/login'
    
    def get_object(self, queryset=None):
        user = self.request.user 
        return user