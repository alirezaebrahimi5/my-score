from rest_framework import permissions, response, status, generics
from rest_framework_simplejwt import tokens

from .models import User 
from .serializers import UserRegisterationSerializer, UserProfileSerializer


####################### Authentication section #######################


class UserLoginAPIView(generics.GenericAPIView):
    """
    An endpoint to login users.
    """


class UserLogoutAPIView(generics.GenericAPIView):
    """
    An endpoint to logout users.
    """

    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()
            return response.Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


class UserRegisterAPIView(generics.CreateAPIView):
    """
    An endpoint to register a user
    """
    
    serializer_class = [UserRegisterationSerializer]
    
    # permission_classes = []
    
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = tokens.RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return response.Response(data, status=status.HTTP_201_CREATED)


class UsreProfileAPIView(generics.RetrieveAPIView):
    """
    An endpoint for users to see their profiles
    """
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = [UserProfileSerializer]
    
    def get(self, request, *args, **kwargs):
        pass
    
    def put(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.data
            return response.Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(status=status.HTTP_404_NOT_FOUND)


####################### Reset password section #######################


class GetUserMobileAPIView(generics.GenericAPIView):
    """
    An endpoint for users to send their mobile accounts
    """
    
    def post(self, request, *args, **kwargs):
        pass
    
    def get(self, request, *args, **kwargs):
        pass


class SendOTPAPIView(generics.GenericAPIView):
    """
    An endpoint for users to the OTP tokens
    """


class ResetPasswordAPIView(generics.GenericAPIView):
    """
    An endpoint for users to reset their passwords
    """
