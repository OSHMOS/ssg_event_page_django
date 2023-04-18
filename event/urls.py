from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import certify


urlpatterns = [
    path('certify/', certify, name='certify')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
