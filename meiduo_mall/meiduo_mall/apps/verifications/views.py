import random, logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_redis import get_redis_connection

from . import contations
from meiduo_mall.libs.yuntongxun.sms import CPP
from celery_tasks.sms.tasks import send_sms_code

logger = logging.getLogger('django')

class SMSCodeView(APIView):
    """
    发送短信验证码
    """
    # 127.0.0.1:8000/sms_codes/(?P<mobile>1[3-9]\d{9})/
    def get(self, request, mobile):
        # 连接到Redis
        redis_conn = get_redis_connection('verify_codes')
        # 读取flag_send标志看是否存在，存在则在同一分钟内不再发短信
        flag = redis_conn.get('flag_%s' % mobile)
        if flag:
            return Response({'message': '发送短信过于频繁'}, status=status.HTTP_400_BAD_REQUEST)
        # 生成短信验证码
        sms_code = '%06d' % random.randint(0, 999999)
        logger.info(sms_code)
        # 把短信验证码存储到Redis
        # redis_conn.setex('key', '过期时间', 'value')
        # pipeline
        pl = redis_conn.pipeline()
        pl.setex('sms_%s' % mobile, contations.SMS_CODE_EXPIRE_TIME, sms_code)
        # 发送短信验证码
        # CPP().send_sms_code(mobile, [sms_code, contations.SMS_CODE_EXPIRE_TIME//60], 1)
        send_sms_code.delay(mobile, sms_code)
        # 设置短信已发发送的标志flag_send，只要标志存在不在发短信
        pl.setex('flag_%s' % mobile, contations.SEND_SMS_CODE_INTERVAL, 1)
        pl.execute()

        # 返回发送成功状态给前端
        return Response({'message': 'ok'})