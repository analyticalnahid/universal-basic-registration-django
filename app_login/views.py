from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

def sign_up(request):
    form = SignUpForm()
    registered = False
    
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
            
    dict = {'form': form, 'registered': registered}
    return render(request, 'app_login/sign_up.html', context=dict)
            

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
    return render(request, 'app_login/sign_in.html', context={'form': form})

@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))