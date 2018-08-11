from django import forms
from calculator.models import Query
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import AppendedText, PrependedText


class PrintForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = '__all__'