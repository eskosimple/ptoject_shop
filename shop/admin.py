from django.contrib import admin
from .models import Course, Category

admin.site.site_header = 'Courses Shop Admin'
admin.site.site_title = 'My Courses'
admin.site.index_title = 'Courses Admin Area'



class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')

class CoursesInLine(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields':['created_at'], 
            'classes': ['collapse']
            })
    ]
    inlines = [CoursesInLine]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course,CourseAdmin )

# Register your models here.
