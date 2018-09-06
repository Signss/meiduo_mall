from django.contrib.auth.backends import ModelBackend
import re

from .models import User

# 自定义jsonwebtoken的认证返回值，主要是为了登录后的状态保持
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }

def get_user_by_count(account):
    """
    根据账号获取user对象
    :param account: 账号，可以是用户名可以是手机号
    :return: User对象或者None
    """
    try:
        if re.match(r'^1[3-9]\d{9}', account):
            # 账号为手机
            user = User.objects.get(mobile=account)
        else:
            # 账号为用户名
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


# 重写authenticate方法实现多账号登陆
class AuthModelBackend(ModelBackend):

    # 重写认证方法
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_count(username)
        if user and user.check_password(password):
            return user

