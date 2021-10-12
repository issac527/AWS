from django.contrib.auth.models import User
from django.db import models

from profileapp.models import Profile
from projectapp.models import Project

LANGUAGE_CHOICES = (('English', 'English'), ('Japanese', 'Japanese'), ('chinese', 'chinese'),
                    ('vietnamese', 'vietnamese'), ('Indonesia', 'Indonesia'), ('arabic', 'arabic'),
                    ('Bengal', 'Bengal'), ('german', 'german'), ('spanish', 'spanish'), ('french', 'french'),
                    ('Hindi', 'Hindi'), ('italian', 'italian'), ('malaysian', 'malaysian'), ('dutch', 'dutch'),
                    ('portukal ', 'portukal '), ('russian', 'russian'), ('thai', 'thai'), ('turkish', 'turkish'))


class FunctionInfo(models.Model):
    # Function 전 입력 데이터
    # 작성자/ 번역 요청 유저
    F_write = models.ForeignKey(User, on_delete=models.CASCADE, related_name='function', null=True)
    # 프로젝트와 연결
    F_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='function', null=True)
    # 번역 게시글 제목
    F_title = models.CharField(max_length=200, null=True)
    # 번역할 이미지
    F_image = models.ImageField(upload_to='images/', null=False)
    # 번역할 언어
    F_language = models.CharField(choices=LANGUAGE_CHOICES, max_length=25, null=False, blank=False)
    # 작성 일자
    F_create_at = models.DateField(auto_now_add=True, null=True)

    # Function 기능에서 도출되는 데이터
    # 이미지에서 검출된 문자 저장
    F_img_txt = models.TextField(null=True)
    # 번역 결과 저장
    F_img_result = models.TextField(null=True)
    # 변역 데이터의 이미지 중심좌표
    F_img_Coordinate = models.TextField(null=True)

    # def save(self, *args, **kwargs):
    #     if self.F_language is None:
    #         self.F_language = self.F_write.profile.language
    #     super(FunctionInfo, self).save(*args, **kwargs)