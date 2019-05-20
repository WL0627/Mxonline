from django.contrib import admin
from .models import Course, Lesson, Video, CourseResource


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'student_nums',
        'fav_nums',
        'image',
        'click_nums',
        'add_time',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'degree')
    readonly_fields = ('student_nums', 'fav_nums', 'click_nums',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'name',
        'add_time',
    )
    list_display_links = ('course',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'lesson',
        'name',
        'add_time',
    )


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'download', 'add_time')
