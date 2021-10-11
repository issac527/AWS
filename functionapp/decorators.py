from django.http import HttpResponseForbidden
from functionapp.models import FunctionInfo


def func_ownership_required(func):
    def decorated(request, *args, **kwargs):
        fc = FunctionInfo.objects.get(pk=kwargs['pk'])
        if not fc.F_write == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
