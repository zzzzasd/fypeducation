from django.contrib import admin
from django.db.models import Count

from .models import User, Classroom, Student, List, Subject, Task, StudClass, Grade

class StudClassAdmin(admin.ModelAdmin):
    list_display=('date', 'daily_attendance', 'classroom', 'display_students', 'students_count',)

    def display_students(self, obj):
        p = Student.objects.filter(studclass=obj.pk)
        return list(p)    

    def get_queryset(self, request):
        return StudClass.objects.annotate(students_count=Count('student'))

    def students_count(self, obj):
        return obj.students_count


class StudentAdmin(admin.ModelAdmin):
    list_display=('name', 'classroom',)

    # def counter_yeah(self, request):
    #     return StudClass.objects.filter(studclass__display_students=name, daily_attendance='present').count()


class GradeAdmin(admin.ModelAdmin):
    list_display=('student', 'study_year', 'term','geography', 'mathematics', 'english', 'malay', 'science',)


# Register your models here.
admin.site.register(User)
admin.site.register(StudClass, StudClassAdmin )
admin.site.register(Classroom)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Grade, GradeAdmin)