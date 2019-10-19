from django.contrib import admin
from wishapp.models import Sosio_model
# Register your models here.
class Sosio_admin(admin.ModelAdmin):
    list_display = ['wish','date']
admin.site.register(Sosio_model,Sosio_admin)
