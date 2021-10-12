from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.urls import reverse

# @method_decorator(login_required, 'get')
# class SubscriptionView(RedirectView):
#
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse('pro')