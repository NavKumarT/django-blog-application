from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages 

from django.contrib.auth.decorators import login_required 



def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()  # saves the data to database 
			username = form.cleaned_data.get('username')  # a dictionary of cleaned data 
			messages.success(request, f'Account created for {username}!')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')