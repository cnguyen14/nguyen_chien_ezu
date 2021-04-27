from django.contrib import admin

# Register your models here.

from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year

admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Section)
admin.site.register(Instructor)
admin.site.register(Registration)
