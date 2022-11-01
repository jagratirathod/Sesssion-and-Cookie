from django.shortcuts import render

# Create your views here.


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,"settestcookie.html")

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request,"checktestcookie.html")

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request,"deltestcookie.html")






