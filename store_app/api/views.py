from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


def index(request):
    return render(request,'store_app/hello.html')

