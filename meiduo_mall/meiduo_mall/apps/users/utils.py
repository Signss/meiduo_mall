
# 自定义jsonwebtoken的认证返回值，主要是为了登录后的状态保持
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }

