from django.urls import path
from . import views
app_name = "schedule_time"

urlpatterns = [
    path('',views.hii)
]
    