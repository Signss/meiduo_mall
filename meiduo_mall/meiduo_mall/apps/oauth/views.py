from rest_framework.views import APIView
from rest_framework.response import Response
from QQLoginTool.QQtool import OAuthQQ
from django.conf import settings

# Create your views here.
# url(r'^qq/authorization/$', views.QQAuthURLView.as_view()),
class QQAuthURLView(APIView):
    """提供QQ登录页面网址
    https://graph.qq.com/oauth2.0/authorize?response_type=code&client_id=xxx&redirect_uri=xxx&state=xxx
    """
    def get(self, request):

        # next表示从哪个页面进入到的登录页面，将来登录成功后，就自动回到那个页面
        next = request.query_params.get('next')
        if not next:
            next = '/'

        # 获取QQ登录页面网址
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET, redirect_uri=settings.QQ_REDIRECT_URI, state=next)
        login_url = oauth.get_qq_url()

        return Response({'login_url':login_url})