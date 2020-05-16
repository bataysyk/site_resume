from django.urls import path
from .views import sign_in, account, user_logout, ajax_username_to_test, ajax_password_to_test, sign_up
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("sign_in/", sign_in),
    path("account/", account),
    path("user_logout/", user_logout),
    path("ajax_username_to_test/", ajax_username_to_test),
    path("ajax_password_to_test/", ajax_password_to_test),
    path("sign_up/", sign_up),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)