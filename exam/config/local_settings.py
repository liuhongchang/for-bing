DEBUG = True
DOMAIN = ''
ALLOWED_HOSTS = ['*']
BANK_REPO = 'C:\\Users\\28708\\Desktop\\exam\\backup'  # 设置题库上传路径
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exam',
        'USER': 'root',
        'PASSWORD': '123456'
    }
}
# send e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST: str = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '2870894607@qq.com'
EMAIL_HOST_PASSWORD = 'oxgqdjfodmemdgdb'
# Email address that error messages come from.
# Default email address to use for various automated correspondence from
# the site managers.
SERVER_EMAIL = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# People who get code error notifications.
# In the format [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
ADMINS = [('ba2870894607@outlook.com'),]
# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS


