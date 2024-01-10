<<<<<<< HEAD
=======
from rest_framework import response, generics, status, permissions

from .models import UserLocation
from .serializers import LocationSerializer

from user.permissions import *


class AllUsersAllLocationsAPIView(generics.GenericAPIView):
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = LocationSerializer
    
    def get(self, request, *args, **kwargs):
        all_u_l = UserLocation.objects.all()
        serializer_u_l = LocationSerializer(all_u_l, many=True)
        return response.Response(serializer_u_l.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        pass


class AllUsersLatestLocationsAPIView(generics.GenericAPIView):
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = LocationSerializer
    
    def get(self, request, *args, **kwargs):
        all_u_l = UserLocation.objects.all().latest()
        serializer_u_l = LocationSerializer(all_u_l, many=True)
        return response.Response(serializer_u_l.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        pass


class AnyUserLocationAPIView(generics.GenericAPIView):
    permission_classes = [IsManagementUser, IsSales_ManagerUser]
    serializer_class = LocationSerializer
    
    def get(self, request, pk, *args, **kwargs):
        all_u_l = UserLocation.objects.get(pk=pk)
        serializer = LocationSerializer(all_u_l)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk, *args, **kwargs):
        return response.Response()

    def put(self, request, pk, *args, **kwargs):
        pass
>>>>>>> f64a207 (adding some of location functionality)
