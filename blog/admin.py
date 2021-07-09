from django.contrib import admin

from .models import *

# admin.site.register(Student)
# admin.site.register(Teacher)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
        list_display = ['id','ism', 'familya', 'yosh', 'telfon', 'yonalish', 'grant']
        list_editable = ['familya', 'telfon']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['ism', 'familya', 'yosh', 'telfon', 'fan']


@admin.register(Xona)
class XonaAdmin(admin.ModelAdmin):
        list_display = ['raqam', 'egasi' ,'parta_soni', 'stul_soni']