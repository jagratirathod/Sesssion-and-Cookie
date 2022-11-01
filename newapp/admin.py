from django.contrib import admin
from django_object_actions import DjangoObjectActions

# Register your models here.

class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
    def imports(modeladmin, request, queryset):
        print("Imports button pushed")

    changelist_actions = ('imports', )