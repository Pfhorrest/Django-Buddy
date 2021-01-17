from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import CustomUserCreationForm, AccountAuthenticationForm
from account.models import Role
from django.forms.utils import ErrorList
from django.contrib.auth.models import Group
import json


# Create your views here.
def login_view(request):
	context = {}
	context['page_title'] = "Login"

	user = request.user

	if user.is_authenticated:
		return redirect("/")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)

		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)

				if user.is_authenticated:
					return redirect('/')
				else:
					print("Not authenticated")

		else:
			context['errors'] = form.errors

	else:
		form = AccountAuthenticationForm()

	context['form'] = form

	return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')




def register_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Register"	
	user = request.user


	roles = Role.objects.all()
	context['roles'] = roles

	if user.is_authenticated:
		return redirect('/')
	else:
		if request.POST:
			form = CustomUserCreationForm(request.POST)
			if form.is_valid:
				form.save()
				return redirect('login')
			else:
				context['errors'] = form.errors
		else:
			form = CustomUserCreationForm()
		
	context['form'] = form	

	return render(request, "account/register.html", context)

    