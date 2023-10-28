from rest_framework import generics, permissions

from .models import LittleURL
from .serializers import LittleURLSerializer


class LittleURLListCreateAPIView(generics.ListCreateAPIView):
    queryset = LittleURL.objects.all()
    serializer_class = LittleURLSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        self.queryset = self.queryset.filter(owner=self.request.user)
        return super().get_queryset()


class LittleURLRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = LittleURL.objects
    serializer_class = LittleURLSerializer    
    lookup_field = 'little_url'
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        self.queryset = self.queryset.filter(owner=self.request.user)
