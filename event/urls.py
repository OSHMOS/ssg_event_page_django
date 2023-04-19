from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import certify, coupon


urlpatterns = [
    path('certify/', certify, name='certify'),
    path('coupon/', coupon, name='coupon'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
