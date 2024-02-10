from django.shortcuts import render, redirect
from .forms import SignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})