from django.urls import path
from . import views
app_name = "send_email_app"

urlpatterns = [
    path('',views.test,name="test"),
    path('sendemail/',views.send_mail_to_all,name="mail")

]
    