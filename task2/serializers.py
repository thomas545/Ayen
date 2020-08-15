from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    current_state = serializers.SerializerMethodField()

    def get_current_state(self, obj):
        return obj.get_state_display()

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "parent",
            "current_state",
        )
        read_only_fields = (
            "id",
            "current_state",
            "uuid",
            "created",
        )

class TaskLinkedSerializer(serializers.ModelSerializer):
    parent = TaskSerializer()
    linked = TaskSerializer(many=True)

    class Meta:
        model = Task
        depth = 3
        fields = (
            "title",
            "description",
            "parent",
            "linked",
        )
        read_only_fields = (
            "id",
            "uuid",
            "created",
            "linked",
        )