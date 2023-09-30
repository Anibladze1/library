from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserSerializer


class RegisterAPIView(APIView):
    """
    API endpoint that allows new users to register.

    **Parameters**:

    - `email`: Email of the user.
    - `password`: Password for the new user.
    - `location`: Location for the new user.

    **Returns**:
    :return
    - `201 Created`: If registration is successful.
    - `400 Bad Request`: If the provided data is invalid.
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    API endpoint for user login.

    Authenticates the user using email and password and returns an access token.

    **Parameters**:

    - `email`: Email of the user.
    - `password`: Password of the user.

    **Returns**:
    :return
    - `200 OK`: If login is successful along with an access and refresh token.
    - `400 Bad Request`: If credentials are invalid.
    """
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # refresh_token = str(refresh.refresh_token)
            return Response({'access_token': access_token, 'refresh_token': str(refresh)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    """
    API endpoint for user logout.

    Ends the user's current session.

    **Returns**:
    :return
    - `200 OK`: If logout is successful.
    """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class DeleteUserAPIView(APIView):
    """
    API endpoint to delete a user.

    Allows a user to delete their own account or lets a superuser delete any user account.

    **Parameters**:

    - `user_id`: ID of the user to be deleted.

    **Returns**:
    :return
    - `200 OK`: If user deletion is successful.
    - `404 Not Found`: If the user with the given ID does not exist.
    - `403 Forbidden`: If the logged-in user is neither the user to be deleted nor a superuser.
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, user_id=None):
        User = get_user_model()
        # Allow a user to delete themselves or allow a superuser to delete any user
        if request.user.id == user_id or request.user.is_superuser:
            try:
                user_to_delete = User.objects.get(id=user_id)
                user_to_delete.delete()
                return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
