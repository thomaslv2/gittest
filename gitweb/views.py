from django.shortcuts import render,HttpResponse,redirect

def index(request):
    print('stash0后')
    print("创建dev分支后master同位置修改")
    return HttpResponse('欢迎登陆首页')
def register(request):
    print('增加dev分支')
<<<<<<< HEAD
    print('gothub后dev第一次输入')
=======
    print("创建bug分支")
    print('gothub后dev1第一次输入')
>>>>>>> bd8770aeedb5a283e077824cae67742e4a8520ac
    return HttpResponse('开发注册页面')

