from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MemberCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in.')
            return redirect('login')
    else:
        form = MemberCreationForm()
    return render(request, 'members/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'members/profile.html')