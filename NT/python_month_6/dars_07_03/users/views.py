from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm



class HomePageView(View):
    def get(self, request):
        return render(request, 'users/home.html')



class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm
        context = {
            "login_form": form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username)

        if len(user) == 0:
            return redirect('login_page')
        else:
            return redirect('home_page')

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm
        context = {
            "register_form": form
        }

        return render(request, 'users/register.html', context)


    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )

        user.set_password(password)
        user.save()
        print("User created successfully")
        return redirect("login_page")
