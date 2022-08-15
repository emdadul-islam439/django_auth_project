from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
def login(request):
    # if request.method == "POST":
    return render(request, "login.html")
