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
        # form에 입력된 데이터 가져옴
        temp_fi = form.save(commit=False)
        temp_fi.F_write = self.request.user
        ###################################
        # 여기에 기능구현한 부분 넣어줄거임
        #         # 기능 구현 후 필드에 올바른 값 넣어주고
        #         # Save하면 번역하면서 도출된 값들을
        #         # DB에 저장할 수 있음
        #         # temp_fi.F_img_txt = 이미지에서 도출된 문자 (한 단어/문장 당 ','로 구분)
        #         # temp_fi.F_img_result = 도출된 문자를 번역한 문자 (한 단어/문장 당 ','로 구분)
        #         # temp_fi.F_img_Coordinate = 이미지에서 도출된 문자의 중심좌표
        #         #                            ("X1/Y1,X2/Y2,X3/Y3...." 이런식으로 '/', ','로 구분)
        ###################################
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
