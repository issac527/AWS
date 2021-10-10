from django.shortcuts import render

# Create your views here.
def Service_page(request):
    return render(request, "serviceapp/service.html")