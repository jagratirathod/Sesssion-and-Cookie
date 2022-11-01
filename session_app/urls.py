from django.urls import path
from . import views
app_name = "session_app"

urlpatterns = [
    path('set/', views.setsession, name='setsession'),
    path('get/', views.getsession, name='getsession'),
    path('del/', views.delsession, name='delsession'),

]
