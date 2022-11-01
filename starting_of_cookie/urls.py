from django.urls import path
from . import views
app_name = "starting_of_cookie"

urlpatterns = [
    path('set/', views.setcookie, name='setcookie'),
    path('get/', views.getcookie, name='getcookie'),
    path('del/', views.delcookie, name='delcookie'),

]
