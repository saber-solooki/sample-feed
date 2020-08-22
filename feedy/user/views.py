import inject
from rest_framework.permissions import AllowAny

from core_architecture.generics import CACreateAPIView
from user.domain.use_cases.create_user import CreateUserUseCase
from user.serializers import CreateAccountSerializer


class AccountView(CACreateAPIView):
    permission_classes = (AllowAny, )

    @inject.autoparams()
    def __init__(self, use_case: CreateUserUseCase, *args, **kwargs):
        super(AccountView, self).__init__(*args, **kwargs)
        self.use_case = use_case
        self.username = None
        self.password = None
        self.serializer = None

    def is_data_valid(self, request):
        self.serializer = CreateAccountSerializer(data=request.data)
        return self.serializer.is_valid()

    def perform_create_data(self, request):
        self.use_case.register_user(self.serializer.validated_data['username'], self.serializer.validated_data['password'])
