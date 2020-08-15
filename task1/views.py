from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from .serializers import MetadataSerializer, DocumentSerializer
from .models import Metadata, Document


class MetadataViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()
    lookup_field = "name"


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = "name"

