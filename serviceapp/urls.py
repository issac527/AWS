from django.urls import path

from serviceapp.views import Service_page

app_name = "serviceapp"

urlpatterns = [
    path("", Service_page, name='service')
]