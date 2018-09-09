# celery启动的入口：创建celery对象，加载celery配置，注册celery任务
from celery import Celery

# 为celery使用django配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'meiduo_mall.settings.dev'

#celery -A celery_tasks.main worker -l info
# 创建celery对象，并起别名，别名没有实际意义，仅仅是celery的名字
celery_app = Celery('mei_duo')
# 加载celery配置：可以得到任务队列的位置
celery_app.config_from_object('celery_tasks.config')
# 注册celery任务
celery_app.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email'])
