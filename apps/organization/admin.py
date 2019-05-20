from django.contrib import admin
from .models import CityDict, CourseOrg, Teacher


# Register your models here.
@admin.register(CityDict)
class CityDictAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
        'add_time',
    )


@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'desc',
        'click_nums',
        'fav_nums',
        'image',
        'address',
        'city',
        'add_time',
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'click_nums',
        'fav_nums',
        'add_time',
    )
