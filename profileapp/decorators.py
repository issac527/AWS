from django.http import HttpResponseForbidden

from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        # 업데이트한 유저와 현재 접속한 유저와 비교
        if not target_profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated