from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User





def registerview(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    template_name = 'Account/registrationform.html'
    context = {'form': form}
    return render(request, template_name, context)


def loginview(request):
    if request.method=='POST':
        U=request.POST.get('u')
        P=request.POST.get('p')

        user=authenticate(username=U,password=P)

        if user is not None:
            login(request,user)
            return redirect('showlist')
        else:
            messages.error(request,'Invalid Credentials')

    template_name='Account/loginform.html'
    context={}
    return render(request,template_name,context)


def logoutview(request):
    logout(request)
    return redirect('login')


