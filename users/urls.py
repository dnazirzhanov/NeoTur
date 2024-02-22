from django.urls import path
from users.views import CreateUsersAPIView, LoginUserView, SetPhoneNumberAPIView, UserProfileAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('api/register/', CreateUsersAPIView.as_view(), name='register'),
    path('api/login/', LoginUserView.as_view(), name='login'),
    path('api/user/info/', UserProfileAPIView.as_view(), name='user-info'),
    path('api/set_phone/', SetPhoneNumberAPIView.as_view(), name="set_user_phone_number"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]