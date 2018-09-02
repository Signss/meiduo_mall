import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django_redis import get_redis_connection

from . import contations
from meiduo_mall.libs.yuntongxun.sms import CPP


class SMSCodeView(APIView):
    """
    发送短信验证码
    """
    # 127.0.0.1:8000/sms_codes/(?P<mobile>1[3-9]\d{9})/
    def get(self, request, mobile):
        # 连接到Redis
        redis_conn = get_redis_connection('verify_codes')
        # 生成短信验证码
        sms_code = '%06d' % random.randint(0, 999999)
        # 把短信验证码存储到Redis
        # redis_conn.setex('key', '过期时间', 'value')
        redis_conn.setex('sms_%s' % mobile, contations.SMS_CODE_EXPIRE_TIME, sms_code)
        # 发送短信验证码
        CPP().send_sms_code(mobile, [sms_code, contations.SMS_CODE_EXPIRE_TIME//60], 1)
        # 返回发送成功状态给前端
        return Response({'message': 'ok'})