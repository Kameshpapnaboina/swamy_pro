from django.contrib import admin
from .models import detailmodel,exammodel

# Register your models here.
class detailadmin(admin.ModelAdmin):
    list_display=['Exam']
class examadmin(admin.ModelAdmin):
    list_display = ['Exam_Type','Time','Feedback']

admin.site.register(detailmodel,detailadmin)
admin.site.register(exammodel,examadmin)
