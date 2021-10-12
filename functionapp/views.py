from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreationForm
from functionapp.decorators import func_ownership_required
from functionapp.forms import FunctionInfoForm
from functionapp.models import FunctionInfo
from Function.input_img import img_translated


# Function main Page로 가기 위한 함수
def function_main_page(request):
    return render(request, "functionapp/FuncionMain.html")


# 번역을 하기 위한 게시글 작성하는 View
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FICreateView(CreateView):
    model = FunctionInfo
    form_class = FunctionInfoForm
    template_name = 'functionapp/create.html'

    def form_valid(self, form):
        # form에 입력된 데이터 가져오면서 임시 저장
        temp_fi = form.save()
        # 임시 저장된 데이터를 지우기 위한 PK을 미리 저장
        F_PK = temp_fi.pk

        # 현재 접속된 User를 작성자로 넘겨줌
        temp_fi.F_write = self.request.user

        # 사용자가 선택한 이미지의 url값을 문자값으로 변환하여 변수에 담아줌
        url = str(temp_fi.F_image)
        # 사용자가 선택한 언어 값을 문자값으로 변환하여 변수에 담아줌
        lang = str(temp_fi.F_language)

        # 이미지 문자 추출 및 번역을 하는 함수를 실행하여 결과값을
        # 변수에 담아줌 / 이미지에서 추출된 문자, 번역한 문자
        img_txt, return_txt = img_translated(url, lang)
        temp_fi.F_img_txt = img_txt
        temp_fi.F_img_result = return_txt
        print(temp_fi.F_img_txt)
        print(temp_fi.F_img_result)

        # 임시로 저장했던 데이터를 DB에서 지워줌
        f_data = FunctionInfo.objects.get(pk=F_PK)
        f_data.delete()

        # 다시 불러와서 DB에 저장
        temp_fi.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('functionapp:detail', kwargs={'pk': self.object.pk})


# 번역을 통해 도출해낸 결과와 함께
# 사용자가 볼 수 있도록 View 생성
class FRDetailView(DetailView, FormMixin):
    model = FunctionInfo
    form_class = CommentCreationForm
    context_object_name = 'target_func'
    template_name = 'functionapp/detail.html'


# 사용자가 올린 번역된 게시글을 지우는 View
@method_decorator(func_ownership_required, 'get')
@method_decorator(func_ownership_required, 'post')
class FuncDeleteView1(DeleteView):
    model = FunctionInfo
    context_object_name = 'target_func'
    success_url = reverse_lazy("functionapp:F_main")
    template_name = 'functionapp/delete.html'


# 한페이지의 리스트에 표현될 게시물 개수 정하기
class FuncListView(ListView):
    model = FunctionInfo
    context_object_name = 'func_list'
    template_name = 'functionapp/list.html'
    paginate_by = 10
