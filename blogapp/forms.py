from django import forms
from .models import detailmodel,exammodel

class detailform(forms.ModelForm):
    class Meta :
        model = detailmodel
        fields = '__all__'

class examform(forms.ModelForm):
    class Meta :
        model = exammodel
        fields ='__all__'
        