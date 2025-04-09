import uuid
from django.utils.deprecation import MiddlewareMixin

USER_KEY = 'uid'
TEN_YEAR = 60 * 60 * 24 * 365 * 10


class UserIDMiddleware(MiddlewareMixin):
    def __int__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEAR, httponly=True)
        return response

    # 获取用户ID
    @staticmethod
    def generate_uid(request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uid
