from django.urls import path
from django.views.generic import TemplateView

from functionapp.views import function_main_page, FICreateView, FRDetailView, FuncDeleteView1, FuncListView

app_name="functionapp"

urlpatterns = [
    # path('list/', FuncListView.as_view(), name='list'),
    path('main/', function_main_page, name="F_main"),

    path('create/', FICreateView.as_view(), name='create'),
    path('detail/<int:pk>', FRDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', FuncDeleteView1.as_view(), name='delete'),
]