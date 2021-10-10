from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import UIUpdateView
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy

has_ownership = [login_required, account_ownership_required]


# 회원가입
class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/create.html'


# 유저의 정보 보여주기
class UserDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


# 유저 정보 변경
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class UIUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = UIUpdateView
    success_url = reverse_lazy('serviceapp:service')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class UserDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    form_class = UIUpdateView
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'