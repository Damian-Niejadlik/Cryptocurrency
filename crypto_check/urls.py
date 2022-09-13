from django.urls import path

from crypto_check.views import check_view, start_view

urlpatterns = [
    path('crypto/', start_view, name="home"),
    path('crypto/<str:name>/<str:currency>/', check_view, name="check"),
]
