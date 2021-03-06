from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    # 判断用户名是否重复
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
    # 判断手机号是否重复
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # 注册
    url(r'^users/$', views.UserView.as_view()),
    # 用户登录
    # url(r'^authentication/$', obtain_jwt_token),
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户个人中心
    url(r'^user/$', views.UserDetailView.as_view()),
    # 设置邮箱
    url(r'^email/$', views.UserEmailView.as_view()),
    # 验证邮箱链接
    url(r'^emails/verification/$', views.VerifyEmailView.as_view()),
]