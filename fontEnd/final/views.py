from django.shortcuts import render
import requests
from users.models import users
import psycopg2
# from bs4 import BeautifulSoup
# import sqlite3
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,"login.html")
def loggedin(request):
    if(request.method=="POST"):
        email=request.POST['username']
        password=request.POST['password']
        if(users.objects.filter(email=email, password=password).exists()):
            t = users.objects.get(email=email)
            print(t.category)
            conn=psycopg2.connect(
            host="localhost",
            database="news_data",
            user="postgres",
            password="1234")
            cur = conn.cursor()
            # # print(cur/)
            cur.execute("SELECT head,news,img FROM " + t.category)
            rows = cur.fetchall()
            # return render(request,"user_news.html")
            return render(request,"user_news.html",{'h':rows,'cat':t.category})
            # print(result)
            # # return render(request,'profile.html',{'objs':result})
        else:
            print("not found")
            # return render(request,'vlogin.html')
            # return render(request,"user_news.html")
def read(request):
    # conn = sqlite3.connect("news_data.db")
    conn=psycopg2.connect(
        host="localhost",
        database="news_data",
        user="postgres",
        password="1234")
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT head,news,img FROM read")
    rows = cur.fetchall()
   
    return render(request,"home.html",{'h':rows})
def registered(request):
    if(request.method=="POST"):
        Name=request.POST['usernamesignup']
        Email=request.POST['emailsignup']
        password=request.POST['passwordsignup']
        Category=request.POST['Category']
        app=users()
        app.name= Name
        app.email= Email
        app.password=password
        app.category=Category
        app.save()
    return render(request,"login.html")
def home(request):
    return render(request,"index.html")
def sports(request):
    conn = psycopg2.connect(
         host="localhost",
        database="news_data",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT Head,News,img FROM sports")
    rows = cur.fetchall()
    return render(request,"home.html",{'h':rows})
def business(request):
    conn = psycopg2.connect(
         host="localhost",
        database="news_data",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT Head,News,img FROM business")
    rows = cur.fetchall()
    return render(request,"home.html",{'h':rows})
   
def movies(request):
    conn = psycopg2.connect(
         host="localhost",
        database="news_data",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT Head,News,img FROM entertainment")
    rows = cur.fetchall()
    return render(request,"home.html",{'h':rows})
    
def politics(request):
    conn = psycopg2.connect(
         host="localhost",
        database="news_data",
        user="postgres",
        password="1234"
    )
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT Head,News,img FROM politics")
    rows = cur.fetchall()
    return render(request,"home.html",{'h':rows})
   