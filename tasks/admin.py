from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):#Aqui añadimos al panel de admin que se vean los campos de solo lectura
    readonly_fields = ("datetime_created",)#SE LE PASA UNA TUPLA
    



# Register your models here.


admin.site.register(Task,TaskAdmin)