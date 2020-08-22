from django.urls import path

from user.views import AccountView
from rest_framework_simplejwt import views as jwt_views

app_name = 'user'

urlpatterns = [
    path('account/', AccountView.as_view(), name='profile'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='obtain_token'),
]
