from django.contrib import admin
from .models import Course, Instructor, Lesson

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor)

