from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}.')
            #group = Group.objects.get(name='Staff')
            #user.groups.add(group)
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')



