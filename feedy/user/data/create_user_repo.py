from django.contrib.auth.models import User

from user.domain.create_user_repo import CreateUserRepo


class CreateUserRepoDBImpl(CreateUserRepo):
    def is_user_name_exist(self, username):
        return User.objects.filter(username__exact=username).exists()

    def create_user(self, username, password):
        User.objects.create_user(username=username, password=password)
