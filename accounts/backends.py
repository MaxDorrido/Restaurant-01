# from django.contrib.auth.models import User


# class Emailbackend(object):
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             user= User.objects.get(email= username)
#         except User.MultipleObjectsReturned:
#             return None
#         except User.DoesNotExist:
#             return None
#         if getattr(user, 'is_active') and user.check_password(password):
#             return user
#         return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

