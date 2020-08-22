import inject
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from general.exceptions import BusinessException
from general.validator import PasswordValidator
from user.data.create_user_repo import CreateUserRepoDBImpl
from user.domain.create_user_repo import CreateUserRepo
from user.domain.use_cases.create_user import CreateUserUseCase
from user.serializers import CreateAccountSerializer


class CreateUserRepoTest(CreateUserRepo):

    def is_user_name_exist(self, username):
        return True

    def create_user(self, username, password):
        pass


class SimplePasswordValidator(PasswordValidator):

    def validate_password(self, value):
        return value


class AccountCreationBusinessTest(TestCase):
    def setUp(self):
        inject.clear_and_configure(
            lambda binder: binder
                .bind(CreateUserRepo, CreateUserRepoTest())\
                .bind(PasswordValidator, SimplePasswordValidator())
            )

    def test_input_serializer_with_username_and_password(self):
        data = {'username': "saber", 'password': "123"}
        serializer = CreateAccountSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_input_serializer_without_username(self):
        data = {'password': "123"}
        serializer = CreateAccountSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_input_serializer_without_password(self):
        data = {'username': "saber"}
        serializer = CreateAccountSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_username_exist(self):
        use_case = CreateUserUseCase()

        self.assertRaises(BusinessException, use_case.register_user, username='saber', password="123")

    def test_username_exception_code_for_username_exist(self):
        use_case = CreateUserUseCase()
        try:
            use_case.register_user("saber", "123")
        except BusinessException as e:
            self.assertEqual(BusinessException.USERNAME_EXIST, e.code)


class AccountCreationInDatabaseTest(TestCase):
    username = "saber"
    password = "123"

    def setUp(self):
        inject.clear_and_configure(
            lambda binder: binder
                .bind(CreateUserRepo, CreateUserRepoDBImpl())\
                .bind(PasswordValidator, SimplePasswordValidator())
            )

        self.create_user_in_db()

    def create_user_in_db(self):
        use_case = CreateUserUseCase()
        use_case.register_user(self.username, self.password)

    def test_is_user_created(self):
        user_object_in_db = User.objects.first()
        self.assertEqual(user_object_in_db.username, self.username)

    def test_is_password_hashed_in_db(self):
        user_object_in_db = User.objects.first()
        self.assertNotEqual(user_object_in_db.password, self.password)
