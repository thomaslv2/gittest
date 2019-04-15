from django.shortcuts import render,HttpResponse,redirect

def index(request):
    print('stash0后')
    print("master和dev第一次合并分之后，dev再修改")
    return HttpResponse('欢迎登陆首页')
def register(request):
    print('增加dev分支')
    return HttpResponse('开发注册页面')

