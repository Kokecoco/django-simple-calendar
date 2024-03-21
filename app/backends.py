# custom_backend.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class CustomEmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, email=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                # メールアドレスのドメインを検証
                if email.endswith('@gll-kaisei-s.sapporo-c.ed.jp') or username.endswith('@giga.sapporo-c.ed.jp'):
                    return user
                else:
                    return None
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        return True
