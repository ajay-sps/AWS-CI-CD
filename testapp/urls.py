from django.urls import path
from testapp.views import home


urlpatterns = [
    path('',home),
]