from django import forms


class AddForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()


class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeated_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password'] != cleaned_data ['repeated_password:']:
            self.add_error('repeated_password', 'Passwords do not match')

        return cleaned_data
    
class HeyYouForm(forms.Form):
    name = forms.CharField()
