from itsdangerous import TimedJSONWebSignatureSerializer as TJSSerializer
from itsdangerous import BadData
from django.conf import settings

# 签名openid
def generate_save_user_token(openid):
    serializer = TJSSerializer(settings.SECRET_KEY, 600)
    data = {'openid': openid}
    token = serializer.dumps(data)
    return token.decode()

# 获取openid
def check_save_user_token(access_token):
    serializer = TJSSerializer(settings.SECRET_KEY, 600)
    try:
        data = serializer.loads(access_token)
        openid = data.get('openid')
    except BadData:
        return None
    else:
        return openid