import inject

from general.exceptions import BusinessException
from general.validator import PasswordValidator
from user.domain.create_user_repo import CreateUserRepo


class CreateUserUseCase:
    @inject.autoparams()
    def __init__(self, repo: CreateUserRepo, password_validator: PasswordValidator):
        self.repo = repo
        self.password_validator = password_validator

    def register_user(self, username, password):
        if self.repo.is_user_name_exist(username):
            raise BusinessException(code=BusinessException.USERNAME_EXIST)

        self.password_validator.validate_password(password)

        self.repo.create_user(username, password)
