from django.urls import path
from . import views
app_name = "cookie_app"

urlpatterns = [
    path('set/',views.settestcookie),
    path('check/',views.checktestcookie),
    path('del/',views.deltestcookie),
]
    