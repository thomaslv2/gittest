from django.shortcuts import render,HttpResponse,redirect

def index(request):
    return HttpResponse('欢迎登陆首页')

