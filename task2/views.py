from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _u
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable, PermissionDenied
from .serializers import TaskSerializer, TaskLinkedSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        task = Task.objects.filter(Q(id=pk)).first()
        if task.state == Task.INPROGRESS:
            serializer = TaskLinkedSerializer(task, context={"request": request})
        else:
            serializer = self.get_serializer(task, context={"request": request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.state != Task.NEW:
            raise NotAcceptable(_u("You can't edit task."))

        if task.state == Task.DONE:
            raise PermissionDenied(_u("Task Done"))

        serializer = self.get_serializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(_u("Task updated successfully!"))
