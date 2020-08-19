from django.shortcuts import render
# from django.http import HttpResponse
from .import models

def home(request):
    # return HttpResponse("welcome to home page")
    return render(request, "tem/home.html")

def about(request):
    # return HttpResponse("hello, goodmorning")
    article = models.Article.objects.all().order_by('date')
    args={'articles':article}
    return render(request, "tem/about.html",args)

