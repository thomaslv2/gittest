from django.shortcuts import render,HttpResponse,redirect

def index(request):
    print('stash0后')
    return HttpResponse('欢迎登陆首页')
def register(request):
    print('增加dev分支')
    return HttpResponse('开发注册页面')

