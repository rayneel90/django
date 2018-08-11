from django import forms
from .models import Query
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import AppendedText, PrependedText

class TLForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('ApplNo','RMName', 'HRMS', 'product', 'sanction_amt',
                  'roi', 'tenure', 'ltv', 'rating', 'profee',
                  'conpay', 'insur', 'other', 'recurr', 'psl', 'agri_psl', 'rrp')
        widgets = {
            'sanction_amt': forms.NumberInput(attrs={'min': 0, 'step': 1000}),
            'roi': forms.NumberInput(attrs={'min': 0, 'max':100, 'step':0.01}),
            'tenure': forms.NumberInput(attrs={'min': 0}),
            'ltv': forms.NumberInput(attrs={'min': 0, 'max':100, 'step':0.01}),
            'profee': forms.NumberInput(attrs={'min': 0, 'max':100, 'step':0.01}),
            'conpay': forms.NumberInput(attrs={'min': 0, 'max':100, 'step':0.01}),
            'insur': forms.NumberInput(attrs={'min': 0, 'step': 100}),
            'other': forms.NumberInput(attrs={'min': 0, 'step': 100}),
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            AppendedText('roi', '%'),
            AppendedText('profee', '%'),
            AppendedText('conpay', '%'),
            AppendedText('tenure', 'months'),
            PrependedText('sanction_amt', '&#8377'),
            PrependedText('insur', '&#8377'),
            PrependedText('other', '&#8377'),
        )
        super(TLForm, self).__init__(*args, **kwargs)

class ODCCForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('ApplNo','RMName', 'HRMS', 'product', 'sanction_amt',
                  'roi', 'utilisation', 'ltv', 'rating', 'profee',
                  'conpay', 'insur', 'other', 'recurr', 'psl', 'agri_psl', 'rrp')
        widgets = {
            'sanction_amt': forms.NumberInput(attrs={'min': 0, 'step': 1000}),
            'roi': forms.NumberInput(attrs={'min': 0}),
            'utilisation': forms.NumberInput(attrs={'min': 0}),
            'ltv': forms.NumberInput(attrs={'min': 0}),
            'profee': forms.NumberInput(attrs={'min': 0}),
            'conpay': forms.NumberInput(attrs={'min': 0}),
            'insur': forms.NumberInput(attrs={'min': 0}),
            'other': forms.NumberInput(attrs={'min': 0}),
        }
    helper = FormHelper()
    helper.layout = Layout(
        AppendedText('roi', '%'),
        AppendedText('profee', '%'),
        AppendedText('conpay', '%'),
        AppendedText('utilisation', '%'),
        PrependedText('sanction_amt', '&#8377'),
        PrependedText('insur', '&#8377'),
        PrependedText('other', '&#8377'),
    )