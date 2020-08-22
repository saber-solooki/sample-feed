from user.data.create_user_repo import CreateUserRepoDBImpl
from user.domain.create_user_repo import CreateUserRepo
from user.domain.use_cases.create_user import CreateUserUseCase


def provide_use_case():
    return CreateUserUseCase()


def provide_repo():
    return CreateUserRepoDBImpl()


def create_user_binder(binder):
    binder.bind_to_provider(CreateUserUseCase, provide_use_case)
    binder.bind_to_provider(CreateUserRepo, provide_repo)
