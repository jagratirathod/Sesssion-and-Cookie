from django.contrib import admin
from . models import *
# Register your models here.

class MyPostAdmin(admin.ModelAdmin):
    list_display = ('post_heading','post_text')
admin.site.register(Post,MyPostAdmin)

class MyLikeAdmin(admin.ModelAdmin):
    list_display = ('post',)
admin.site.register(Like,MyLikeAdmin)

