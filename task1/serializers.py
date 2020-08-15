from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import Metadata, Document


class UserLoginSerializer(LoginSerializer):
    username = None


class UserRegisterSerializer(RegisterSerializer):
    username = None


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = (
            "name",
            "string",
        )

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "name",
            "files",
        )

