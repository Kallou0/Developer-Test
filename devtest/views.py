from django.shortcuts import render, HttpResponse, redirect

# Creating views:
def index(request):
    return render(request, 'home.html')
