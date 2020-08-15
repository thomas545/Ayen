from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('metadata', views.MetadataViewSet, basename="metadata")
router.register('documents', views.DocumentViewSet, basename="documents")



urlpatterns = [
    # path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
]

# urlpatterns += router.urls

