from django.contrib import admin
from .models import Student,Book
# Register your models here.
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','cohort']
@admin.register (Book)
class Bookadmin(admin.ModelAdmin):
    list_display = ['title','no_of_pages','author','owner',]
    search_fields = ['title','author']
    list_per_page = 10
