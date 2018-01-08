from django.contrib import admin

from .models import List, Subject, Task

# Register your models here.
#admin.site.register(User)
admin.site.register(Subject)
admin.site.register(List)
admin.site.register(Task)
