from django.db import models
from django.contrib.auth.models import AbstractUser
from itsdangerous import TimedJSONWebSignatureSerializer as TJSSerializer
from django.conf import settings


class User(AbstractUser):
    # 构建用户模型类
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    # 添加邮箱是否验证字段
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name

    def generate_verify_email_url(self):
        serializer = TJSSerializer(settings.SECRET_KEY, 3600*24)
        data = {'user_id': self.id, 'email': self.email}
        token = serializer.dumps(data).decode()
        verify_url = 'http://www.meiduo.site:8080/success_verify_email.html?token=' + token
        return verify_url