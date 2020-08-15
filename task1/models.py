from django.db import models
from core.models import TimeStampedModel, UUIDModel


def document_file_path(instance, filename):
    return f"Document/{instance.name}/{filename}"


class Metadata(TimeStampedModel, UUIDModel):
    name = models.CharField(max_length=250)
    string = models.TextField()

    class Meta:
        verbose_name_plural = "Metadata"

    def __str__(self):
        return self.name


class Document(TimeStampedModel, UUIDModel):
    name = models.CharField(max_length=250)
    files = models.FileField(upload_to=document_file_path)

    class Meta:
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.name
