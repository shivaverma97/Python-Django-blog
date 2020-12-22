from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserProfileUpdateForm, ProfilePicUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You can Login Now.')
            return redirect('login')
    else:
        form = UserRegisterationForm()
    return render(request,'users/register.html',{'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserProfileUpdateForm(request.POST, instance=request.user)
        p_form = ProfilePicUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Account Info has been updated!')
            return redirect('profile')

    else :
        u_form = UserProfileUpdateForm(instance=request.user)
        p_form = ProfilePicUpdateForm(instance=request.user.profile)

    context ={'u_form':u_form,
    'p_form':p_form }

    return render(request,'users/profile.html', context)
