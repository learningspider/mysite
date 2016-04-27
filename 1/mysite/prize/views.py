#_*_coding:utf-8_*_
from django.shortcuts import render,HttpResponseRedirect
from myusers.models import MyUser
from hashlib import sha1
import os,time,datetime,string
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


#create_session = lambda : sha1('%s%s' %(os.urandom(16),time.time())).hexdigest()

def index(request):
    if request.user.is_authenticated():
        return render(request,'prize/index.html',{'user':request.user})
    return render(request,'prize/index.html')

def shop(request):
    return render(request,'prize/index.html')

def acc_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        userName = request.POST.get('userName')
        try:
            getuser=MyUser.objects.get(email=userName)
            if getuser:
                login_err = "用户已存在！"
                return  render(request,'prize/register.html', {'login_err':login_err})
        except:
            pass


        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')
        if (password1==password2):
            password = password1
        else:
            login_err = "Wrong username or password!"
            return  render(request,'prize/register.html', {'login_err':login_err})
        datetime1 = datetime.date.today()
        user1=MyUser.objects.create_user(email=userName,password=password,name="name",date_of_birth=datetime1)

        user = authenticate(username=userName,password=password1)
        if user is not None:
            login(request,user)

            return HttpResponseRedirect('/')

        else:
            login_err = "Wrong username or password!"
            return  render(request,'prize/register.html', {'login_err':login_err})
    return render(request,'prize/register.html')

def acc_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        print userName,password
        user = authenticate(username=userName,password=password)
        print user
        if user is not None:
            login(request,user)

            return HttpResponseRedirect('/')

        else:
            login_err = "Wrong username or password!"
            return  render(request,'prize/login.html', {'login_err':login_err})

    return render(request,'prize/login.html')

@login_required
def acc_logout(request):
    logout(request)
    return  HttpResponseRedirect("/")
'''def acc_login(requeset):
    login_err = ''
    if requeset.method == 'POST':
        username = requeset.POST.get('email')
        password = requeset.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(requeset,user)

            return HttpResponseRedirect('/')

        else:
            login_err = "Wrong username or password!"
    return  render(requeset,'login.html', {'login_err':login_err})'''

@login_required
def profile(request):
    return render(request,'prize/profile.html',{'user':request.user})


@login_required
def MyAddressManager(request):
    return render(request,'prize/MyAddressManager.html',{'user':request.user})

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        oldpassword = string.strip(request.POST.get('OldPassword'))
        usernow = authenticate(username=request.user.email,password=oldpassword)

        if usernow:
            newpassword = string.strip(request.POST.get('NewPassword'))
            if len(newpassword)<6:
                login_err = "密码长度小于6位!"
                return  render(request,'prize/ChangePassword.html', {'login_err':login_err})
            confirmpassword = string.strip(request.POST.get('ConfirmPassword'))
            if newpassword and confirmpassword and newpassword != confirmpassword:
                login_err = "Wrong password!"
                return  render(request,'prize/ChangePassword.html', {'login_err':login_err})
            else:
                usernow.set_password(newpassword)
                usernow.save()

                login_err = "密码修改成功!"
                return  render(request,'prize/ChangePassword.html', {'login_err':login_err})
        else:
            login_err = "旧密码输入错误!"
            return  render(request,'prize/ChangePassword.html', {'login_err':login_err})
    return render(request,'prize/ChangePassword.html',{'user':request.user})



@login_required
def MyOrder(request):
    return render(request,'prize/MyOrder.html',{'user':request.user})

@login_required
def MyRefunds(request):
    return render(request,'prize/MyRefunds.html',{'user':request.user})

@login_required
def MyReservation(request):
    return render(request,'prize/MyReservation.html',{'user':request.user})

