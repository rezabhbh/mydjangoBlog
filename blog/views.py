from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("welcome to home page")
    return render(request,"homee.html")

# def about(request):
#     # return HttpResponse("hello, goodmorning")
#     return render(request, "./about.html")

