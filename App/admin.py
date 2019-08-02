from django.contrib import admin

# Register your models here.
from .models import Thing, Text
admin.site.register(Thing)
admin.site.register(Text)