# Template에서 python 함수를 사용하기위해
# 사용자 정의 태그를 정의해줌

from django import template

register = template.Library()


# split함수
@register.filter(name='split')
def split(value, arg):
    return value.split(arg)


# 숫자만큼의 배열 생성
@register.filter(name='f_range')
def f_range(value):
    return range(len(value))


# 리스트의 인덱스를 사용
@register.filter(name='f_index')
def f_index(value, index):
    return value[index]