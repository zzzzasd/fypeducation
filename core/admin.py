from django.contrib import admin

from .models import Classroom, Student, Attendance, List, Subject, Task

class AttendanceAdmin(admin.ModelAdmin):
  list_filter = ('student__classroom',)
  raw_id_admin = ('student',)
# Register your models here.
#admin.site.register(User)
admin.site.register(Subject)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Attendance)