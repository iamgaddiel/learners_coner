from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework import status
from rest_framework.response import Response
from virtual_tour.models import VirtualTour
from virtual_tour.serializers import VirtualTourSerializer


class VirtualTourViewSet(viewsets.ModelViewSet):
    queryset = VirtualTour.objects.all()
    serializer_class = VirtualTourSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

class VirtualTourClientView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = VirtualTour.objects.all()
        sq = VirtualTourSerializer(queryset, many=True)
        return Response(sq.data, status=200)