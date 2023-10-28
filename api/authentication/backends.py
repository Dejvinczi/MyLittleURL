import jwt

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import authentication, exceptions

User = get_user_model()


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        _, token = auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(username=payload['username'])
            return user, token
        except jwt.DecodeError as exc:
            raise exceptions.AuthenticationFailed('Your token is invalid')
        except jwt.ExpiredSignatureError as exc:
            raise exceptions.AuthenticationFailed('Your token is expired')
