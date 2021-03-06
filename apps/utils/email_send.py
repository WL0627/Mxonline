from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from Mxonline.settings import EMAIL_FROM


# 生成验证码
def random_str(randomlength):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 发送邮件
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = '慕学在线网注册激活链接'
        email_body = '请点击下面链接激活你的账号：http://127.0.0.1:8000/reset/{0}'.format(
            code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email, ])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '慕学在线网密码重置链接'
        email_body = '请点击下面链接激活你的账号：http://127.0.0.1:8000/reset/{0}'.format(
            code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email, ])
        if send_status:
            pass


