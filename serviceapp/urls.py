from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from serviceapp.views import Service_page

app_name = "serviceapp"

urlpatterns = [
    path("", Service_page, name='service')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)