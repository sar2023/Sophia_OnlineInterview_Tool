from django.shortcuts import render,redirect
from accounts.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from assessments.views import welcomeScreen
from django.contrib.auth.decorators import login_required


# Create your views here.

def home (request):
	if request.user.is_authenticated:
		return redirect('afterlogin')
	else:
		return render(request,'index.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('welcome')
	else:
		form = UserRegistrationForm()
		if request.method == 'POST':
			form = UserRegistrationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)
@login_required(login_url='login')
def afterlogin(request):
	return render(request,'afterlogin.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('welcome')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('afterlogin')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return render(request,'logout.html')
