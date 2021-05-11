# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, NameForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success
})

def mysqllogin(request):
    import mysql.connector
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
           ###if form.db.value="MySql"
            host = form.cleaned_data.get('host')
            user = form.cleaned_data.get('userid')
            password = form.cleaned_data.get('password')
            print(host,user,password)
            cnx = mysql.connector.connect(user=user, password=password,
                              host=host,
                              )

            cursor = cnx.cursor()
            databases=[]
            cursor.execute("SHOW DATABASES")
            for row in cursor.fetchall():
                databases.append(row[0])
                print(row[0])

            ###return HttpResponseRedirect('showdb.html', request.POST['host'])
   ### else:
    print(request.GET)
       ### html_template = loader.get_template( 'page-500.html' )###
        ###form=NameForm()
    ###return render(request,"database.html", {{'host':host,'userid':user,'password':password}})
    return render(request,"showdb.html",{'databases':databases})

