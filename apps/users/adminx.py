import xadmin
from .models import UserProfile, EmailVerifyRecord, Banner
from xadmin import views


# Register your models here.
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '慕学在线后台'
    site_footer = '慕学在线'
    menu_style = 'accordion'


class UserProfileAdmin(object):
    list_display = ('nick_name', 'birthday', 'gender', 'address', 'mobile', 'image')


class EmailVerifyRecordAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time',)


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'index', 'add_time',)


# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
