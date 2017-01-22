from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<a href='/blog/about'>About</a><br/><br/>Startsev's Blog")

def about(request):
    return HttpResponse("<a href='/blog'>Home</a><br/><br/>About this blog")
