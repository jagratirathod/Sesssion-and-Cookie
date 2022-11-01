from django.urls import path
from . import views
app_name = "demoapp"

urlpatterns = [
    path('', views.GenerateRandomUserView.as_view(),name="generate"),
    path('hii',views.hii)
]
    