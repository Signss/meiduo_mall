from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .serializers import CreateUserSerializer, UserDetailSerializer, EmailSerializer
from .models import User

# Create your views here.
# url(r'^users/$', views.UserView.as_view()),
class UserView(CreateAPIView):
    """用户注册"""

    # 指定序列化器：剩下的CreateAPIview做完了
    serializer_class = CreateUserSerializer


# url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
class MobileCountView(APIView):
    """判断手机号是否重复"""
    def get(self, request, mobile):
        # 使用mobile作为条件查询满足条件的记录的数量
        count = User.objects.filter(mobile=mobile).count()
        # 构造响应数据
        data = {
            'mobile': mobile,
            'count': count
        }
        # 响应数据
        return Response(data)

# url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
class UsernameCountView(APIView):
    """判断用户名是否存在"""

    def get(self,request, username):
        # 使用username作为条件查询满足条件的记录的数量
        count = User.objects.filter(username=username).count()

        # 构造响应数据
        data = {
            'username':username,
            'count':count
        }

        # 响应数据
        return Response(data)


# 用户个人中心
class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    # 因为没有传入id
    def get_object(self, *args, **kwargs):
        return self.request.user


# 保存email
class UserEmailView(UpdateAPIView):
    serializer_class = EmailSerializer
    permission_classes = [IsAuthenticated]

    # 因为没有传入id
    def get_object(self, *args, **kwargs):
        return self.request.user


# 验证邮箱链接
# url(r'^emails/verification/$', views.VerifyEmailView.as_view()),
class VerifyEmailView(APIView):

    def get(self, request):
        # 获取token值
        token = request.query_params.get('token')
        if not token:
            return Response({'message': '缺少参数'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.check_verify_email_token(token)
        if not user:
            return Response({'message': '缺少参数'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.email_active = True
            user.save()
            return Response({'message': 'ok'})

