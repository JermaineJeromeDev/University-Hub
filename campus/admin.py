from django.contrib import admin
from .models import Semester, Professor, Student, StudentIDCard, Course, CourseDescription

# Register your models here.

admin.site.register(Semester)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(StudentIDCard)
admin.site.register(Course)
admin.site.register(CourseDescription)