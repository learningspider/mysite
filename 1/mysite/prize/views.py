from django.shortcuts import render
from hashlib import sha1
import os,time

create_session = lambda : sha1('%s%s' %(os.urandom(16),time.time())).hexdigest()

def index(request):
    return render(request,'prize/index.html')

def shop(request):
    return render(request,'prize/index.html')

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
