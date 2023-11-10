from django.urls import path
from .views import AuthProxyView


urlpatterns = [
    path('auth/', AuthProxyView.as_view(), name='auth-proxy'),
]
