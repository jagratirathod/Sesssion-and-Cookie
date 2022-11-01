from django.http import HttpResponse
from django.shortcuts import render
from schedule_time. tasks import test_func
from . tasks import send_mail_func


# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("succes Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

