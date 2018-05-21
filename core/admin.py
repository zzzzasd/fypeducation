from django.contrib import admin

from .models import Classroom, Student, Attendance, List, Subject, Task, StudClass

# class AttendanceAdmin(admin.ModelAdmin):
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == "student":
    #         kwargs["queryset"] = Student.objects.filter(semester_average)
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)



# Register your models here.
#admin.site.register(User)
admin.site.register(Subject)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Classroom)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(StudClass)