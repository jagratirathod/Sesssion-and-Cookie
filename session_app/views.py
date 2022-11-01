from email.policy import default
from django.shortcuts import render

# Create your views here.

# def setsession(request):
#     request.session['name']='riya'
#     request.session['lname']='rathod'
#     return render(request,"setsessions.html")

# def getsession(request):
#     name = request.session['name']
#     lname = request.session['lname']
#     keys = request.session.keys()
#     items = request.session.items()
#     values = request.session.values()
#     age = request.session.setdefault('age','26')
#     # name=request.session.get('name',default='Guest')
#     return render(request,"getsessions.html",{'name':name , 'lname':lname , 'keys':keys , 'items':items, 'values':values,'age':age})

# # def delsession(request):
#     if 'name' in request.session:
#         del request.session['name']
#     return render(request,'delsessions.html')


def delsession(request):
    request.session.flush()
    return render(request,'delsessions.html')
    
# more method 
def setsession(request):
    request.session['name']='riya'
    request.session.set_expiry(0)
    return render(request,"setsessions.html")
  
def getsession(request):
    name = request.session['name']
    request.session.clear_expired()
    return render(request,"getsessions.html",{'name':name })



