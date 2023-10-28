import jwt

from rest_framework.response import Response
from rest_framework import status, generics, permissions

from django.contrib import auth
from django.conf import settings

from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects

    def post(self, request):
        request_data = request.data
        username = request_data.get('username')
        password = request_data.get('password')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.SECRET_KEY, algorithm="HS256")
            serializer = self.serializer_class(user)

            return Response({**serializer.data, 'token': auth_token}, status=status.HTTP_200_OK)

        return Response({'Invalid credentials!'}, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects
    permission_classes = (permissions.IsAuthenticated, )


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'username'
