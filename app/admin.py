from django.contrib import admin

# Register your models here.


from app.models import *
admin.site.register(Topic)

def __str__ (self):
     return Topic.topic_name

admin.site.register(Webpage)

def __str__ (self):
    return Webpage.webpage_name

admin.site.register(AccessRecord)

def __str__ (Self):
    return AccessRecord.accessrecord_author

