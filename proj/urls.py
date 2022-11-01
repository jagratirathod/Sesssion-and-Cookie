from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demoapp/', include('demoapp.urls')),
    path('salry/', include('salry.urls')),
    path('post/', include('post.urls')),
    path('schedule_time/', include('schedule_time.urls')),
    path('session_app/', include('session_app.urls')),
    path('cookie_app/', include('cookie_app.urls')),
    path('starting_of_cookie/', include('starting_of_cookie.urls')),
]
