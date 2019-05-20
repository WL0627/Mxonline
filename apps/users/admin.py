from django.contrib import admin
from .models import UserProfile, EmailVerifyRecord, Banner


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'birthday', 'gender', 'address', 'mobile', 'image')


@admin.register(EmailVerifyRecord)
class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('code', 'email', 'send_type', 'send_time',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url', 'index', 'add_time',)
