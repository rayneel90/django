from django import forms
from crispy_forms.helper import FormHelper
from .models import Query

class QueryForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = ('typ', 'ApplNo','RMName', 'HRMS', 'product', 'sanction_amt',
                  'roi', 'tenure', 'utilisation', 'ltv', 'rating', 'profee',
                  'conpay', 'insur', 'other', 'recurr', 'psl', 'agri_psl', 'rrp')
