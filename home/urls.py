from django.urls import path
from .views import home, price_list_count, resume
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home),
    path("resume", resume),
    path("home/", home),
    path('price/<pk>/', price_list_count, name='price_list_count'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)