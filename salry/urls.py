from django.urls import path
from . import views
app_name = "salry"

urlpatterns = [
    path('',views.hello)
]
    