from django.conf.urls import url
from . import views

urlpatterns = [
    # QQ扫码登录界面
    url(r'^qq/authorization/$', views.QQAuthURLView.as_view()),
    # QQ扫码回调，绑定openid
    url(r'^qq/user/$', views.QQAuthUserView.as_view()),
]