from abc import ABCMeta, abstractmethod


class CreateUserRepo(metaclass=ABCMeta):
    @abstractmethod
    def is_user_name_exist(self, username):
        pass

    @abstractmethod
    def create_user(self, username, password):
        pass
