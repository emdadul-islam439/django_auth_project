from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "index.html")


def loginUser(request):
    if request.method == "POST":
        user_name = request.POST.get('userName')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")
        
    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")
