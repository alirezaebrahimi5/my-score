from rest_framework import generics, permissions, response, status

from .serializers import *

from user.permissions import *


class UserDailyWorkAPIView(generics.GenericAPIView):
    serializer_class = UserTimeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        return response.Response() 
    
    def get(self, request, *args, **kwargs):
        return response.Response()


class UserScoreAPIView(generics.GenericAPIView):
    serializer_class = UserGivenScoreSerializer
