from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from food.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'food/home.html')


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                #request,
                username = username,
                password = password
            )
            login(request, user)
            #return redirect('/food')
            return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'food/reg_form.html', args)
@login_required
def profile(request):
    args = {'user': request.user}
    return render(request ,'food/profile.html', args)