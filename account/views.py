from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.admin import User
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import UserFrom

# Create your views here.
def sign_in(request):
    if request.method == "GET":
        return render(request, "account/sign_in.html")
    if request.method == "POST":
        username_q = request.POST.get("inputUsername")
        password_q = request.POST.get("inputPassword")
        if username_q and password_q:
            print(username_q)
            print(password_q)
            user = authenticate(username=username_q, password=password_q)
            print(user)
            if user is not None:
                login(request, user)
                print(user)
                return redirect("/home/")
            else:
                return HttpResponse("User not authenticate")
        return HttpResponse("Форма не заповнена")


def account(request):
    return render(request, "account/account.html")


def user_logout(request):
    logout(request)
    return redirect("/home/")


def ajax_username_to_test(request):
    result = dict()
    login = request.GET.get("login")
    if User.objects.filter(username=login).exists():
        result["result"] = "Exists"
    else:
        result["result"] = "Free"
    return JsonResponse(data=result)


def ajax_password_to_test(request):
    result = dict()
    password = request.GET.get("password")
    print(password)
    if User.objects.filter(password=password).exists():
        print("OK")

        result["result"] = "Exists"
    else:
        print("NOT OK")

        result["result"] = "Free"
    return JsonResponse(data=result)


def sign_up(request):
    data = dict()
    form = UserFrom(request.POST or None, request.FILES or None)
    data["form"] = form
    if request.method == "GET":
        return render(request, "account/sign_up.html", context=data)
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")
        if username and email and password_1 and password_2:
            print(password_1)
            print(password_2)
            if password_1 == password_2:
                user = User.objects.create_user(username=username, email=email, password=password_1)
                # user = User(
                #     username=username,
                #     email=email,
                #     password=password_1,
                # )
                user.save()
        return redirect("/home/")
