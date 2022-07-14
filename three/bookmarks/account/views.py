from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from django.core.exceptions import PermissionDenied
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render
from .models import Activity
from .forms import ActivityForm
from project.forms import ProjectForm
from project.models import Project


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    new_Activity = None
    ido = request.user
    print(ido)
    data = Activity.objects.filter(name__assigned=ido)
    print(data)
    if request.method == 'POST':
        # A Activity was posted 
        Activity_form = ActivityForm(data=request.POST)
        if Activity_form.is_valid():
            # Create Activity object but don't save to database yet
            new_Activity = Activity_form.save(commit=False)
            # Save the Activity to the database
            new_Activity.save()
    else:
        Activity_form = ActivityForm()
    #if the user is admin
    if request.user.is_superuser:
        data = Activity.objects.all()
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'new_Activity': new_Activity, 'Activity_form': Activity_form, 'data':data})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})



    