import xadmin
from .models import CityDict, CourseOrg, Teacher


# Register your models here.

class CityDictAdmin(object):
    list_display = (
        'name',
        'desc',
        'add_time',
    )



class CourseOrgAdmin(object):
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


class TeacherAdmin(object):
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
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
