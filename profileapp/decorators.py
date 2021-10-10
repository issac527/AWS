from django.http import HttpResponseForbidden

from profileapp.models import Profile

def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        # 업데이트한 유저와 현재 접속한 유저와 비교
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            # 권한이 없으면 경고창을 보내줌
            return HttpResponseForbidden()
    return decorated