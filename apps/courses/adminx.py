import xadmin

from .models import Course, Lesson, Video, CourseResource


# Register your models here.

class CourseAdmin(object):
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


class LessonAdmin(object):
    list_display = (
        'course',
        'name',
        'add_time',
    )
    list_display_links = ('course',)


class VideoAdmin(object):
    list_display = (
        'lesson',
        'name',
        'add_time',
    )


class CourseResourceAdmin(object):
    list_display = ('course', 'name', 'download', 'add_time')


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
