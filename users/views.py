from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
