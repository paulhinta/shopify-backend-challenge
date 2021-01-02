from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberCreationForm, MemberUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')
            #redirecting allows user to avoid "are you sure you want to resubmit form"
            #ie. only one post request is run, not two
    else:
        form = MemberCreationForm()
    return render(request, 'members/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        #passing in post data for both forms + additional file data for profile form
        update  = MemberUpdateForm(request.POST, instance=request.user)
        uimage  = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #we can populate these forms this way because these are model forms
        #ie. they expect these kinds of inputs
        if update.is_valid() and uimage.is_valid():
            update.save()
            uimage.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        update  = MemberUpdateForm(instance=request.user)
        uimage  = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update' : update,
        'uimage' : uimage
    }
    return render(request, 'members/profile.html', context)