from django.contrib import admin
from .models import User, Subject, List

# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(List)