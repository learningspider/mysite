from django.shortcuts import render,HttpResponseRedirect
from hashlib import sha1
import os,time
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
    return render(request,'prize/register.html')

def acc_login(request):
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
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
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
    return render(request,'prize/ChangePassword.html',{'user':request.user})

@login_required
def MyOrder(request):
    return render(request,'prize/MyOrder.html',{'user':request.user})

