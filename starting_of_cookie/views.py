from datetime import datetime, timedelta
from urllib import response
from django.shortcuts import render

# Create your views here.


# def setcookie(request):
#     response = render(request , "setcookie.html")
#     response.set_cookie('name', 'sonam')
#     return response  

def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name',"Guest")
    return render(request,"getcookie.html",{"name":name})

def delcookie(request):
    response = render(request,"delcookie.html")
    response.delete_cookie('name')
    return response

# def setcookie(request):
#     response = render(request , "setcookie.html")
#     response.set_cookie('name', 'sonam' , max_age=60)
#     return response  

# def setcookie(request):
#     response = render(request , "setcookie.html")
#     response.set_cookie('lname', 'rathod' , expires= datetime.utcnow()+timedelta(days=2))
#     return response  

# salt
def setcookie(request):
    response = render(request , "setcookie.html")
    response.set_signed_cookie('name', 'riya' ,salt="nm")
    return response  

def getcookie(request):
    name = request.get_signed_cookie('name',salt="bgcgbfnm")
    return render(request,"getcookie.html",{"name":name})