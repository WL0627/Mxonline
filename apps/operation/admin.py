from django.contrib import admin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


# Register your models here.
@admin.register(UserAsk)
class UserAskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile',
        'course_name',
        'add_time',
    )


@admin.register(CourseComments)
class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'course',
        'comments',
        'add_time',
    )


@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'fav_id',
        'fav_type',
        'add_time',
    )


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'message',
        'has_read',
        'add_time',
    )

@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'add_time', )