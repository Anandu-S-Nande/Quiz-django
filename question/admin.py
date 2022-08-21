from django.contrib import admin
from .models import Exam


# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id','question')
    
admin.site.register(Exam,ExamAdmin)
