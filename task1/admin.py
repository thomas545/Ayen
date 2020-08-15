from django.contrib import admin
from .models import Metadata, Document


@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    readonly_fields = (
        "uuid",
        "created",
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = (
        "uuid",
        "created",
    )

