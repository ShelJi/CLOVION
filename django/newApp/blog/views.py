from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")

def details(request):
    return render(request, "detail.html")

def redirect_to(request):
    return redirect(reverse("blog:index"))

