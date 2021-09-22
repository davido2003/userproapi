from django.contrib import admin
from django.db import models
from . models import Profile
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','email')
    search_fields = ('title','email')
    list_per_page=2
# Register your models here.
admin.site.register(Profile,ProfileModelAdmin)