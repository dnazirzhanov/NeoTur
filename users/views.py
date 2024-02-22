from django.shortcuts import render
from .models import User
from .serializers import UserCreateSerializer, PhoneNumberSerializer
from rest_framework.generics import CreateAPIView


class CreateUsers(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class LoginUserView(views.APIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            return Response({'user_id': user.id, 'access': access, 'refresh': str(refresh)},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class SetPhoneNumberAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        serializer = PhoneNumberSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        verify_code = "1234"
        user.verify_code = verify_code
        user.save()
        return Response(
            {'message': 'Код отправлен на ваш номер.'},
            status=status.HTTP_200_OK
        )