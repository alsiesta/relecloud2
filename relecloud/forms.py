from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Destination

class DestinationForm(forms.ModelForm):  # Use forms.ModelForm here
    class Meta:
        model = Destination
        fields = ['name', 'description', 'rank']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))