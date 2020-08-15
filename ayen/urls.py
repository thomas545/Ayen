from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import routers
from task1.urls import router as task1_router
from task2.urls import router as task2_router

router = routers.DefaultRouter()

router.extend(task1_router)
router.extend(task2_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('task1.urls')),
    path('', include('task2.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)