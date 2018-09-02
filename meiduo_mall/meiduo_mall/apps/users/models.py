from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 构建用户模型类
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')


    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name
