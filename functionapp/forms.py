from django.forms import ModelForm

from functionapp.models import FunctionInfo


class FunctionInfoForm(ModelForm):
    class Meta:
        model = FunctionInfo
        fields = ['F_title', 'F_image', 'F_language']