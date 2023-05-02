from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.
def register(request):
    if request.method != 'POST':
        form = RegisterUserForm()
    else:
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            auth_user = authenticate(username=new_user.username, email=new_user.email, password=request.POST['password2'])
            if auth_user is not None:
                login(request,auth_user)
                return HttpResponseRedirect(reverse('book_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html', context)