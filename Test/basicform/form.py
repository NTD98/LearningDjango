from django import forms
from basicform.models import User
class FormName(forms.ModelForm):
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['vertify_email']

        if email != vemail:
            raise forms.ValidationError("email missmatch!!!")
    class Meta:
        model = User
        fields = '__all__'