from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from details.models import User


# Create your views here.
class UserReg(View):

    def get(self, request):
        return render(request, 'user_reg.html')

    def post(self, request):
        try:
            data = request.POST.dict()
            data.pop('csrfmiddlewaretoken')

            User.objects.create_user(**data)

            return redirect('/login')
        except Exception as e:
            print(e)
            return render(request, 'user_reg.html')


class UserLogin(View):

    def get(self, request):
        return render(request, 'user_log.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        return HttpResponse('invalid Details')


# class UserProfile(View):
#     def get(self, request):
#         return render(request, 'room.html')
class UserProfile(View):
    def get(self, request):
        return render(request, 'user_profile.html')


def user_logout(request):
    logout(request)
    return redirect('login')

