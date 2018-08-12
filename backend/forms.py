from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'file',
            Submit('submit', 'Submit')
        )
        super(UploadFileForm, self).__init__(*args, **kwargs)