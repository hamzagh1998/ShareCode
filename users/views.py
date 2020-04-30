from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .forms import LoginForm, RegisterForm, AccountForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from post.models import Post
from .models import Profile


def registerView(request):

    if request.user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Account Created For {}!'.format(form.cleaned_data['username']))
            return redirect('users:login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form':form})

def loginView(request):

    if request.user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form':form})

@login_required
def logOut(request):
    logout(request)
    return redirect('index')

def completeProfile(request):

    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.user.profile.first_name:
        print('done1')
        return redirect('index')

    if request.POST:
        form = AccountForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if form.is_valid():
            form.save(commit=True)
            print('done2')
            return redirect('index')
    else:
        form = AccountForm(instance=request.user.profile)

    return render(request, 'users/complete_profile.html', {'form':form})

def profileView(request, id):

    if not request.user.is_authenticated:
        return redirect('login')

    if id is not request.user.id:
        return HttpResponse('Error, This is not your profile!')

    user = get_object_or_404(User, id=id)
    profile = Profile.objects.get(id=user.id)
    user_posts = Post.objects.filter(author=user)

    user_form = UserForm(initial={'email':request.user.email})
    profile_form = AccountForm(initial={'first_name':profile.first_name,
                                'last_name':profile.last_name,
                                'photo':profile.photo,
                                'phone':profile.phone})

    if request.POST:
        profile_form = AccountForm(request.POST or None, request.FILES or None, instance=profile)
        user_form = UserForm(request.POST or None, request.FILES or None, instance=user)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')

    return render(request, 'users/user_profile.html', {'profile_form':profile_form, 'user_form':user_form, 'user_posts':user_posts})
