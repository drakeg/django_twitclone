from django import forms
from .models import Profile, Tweet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.replied_to_tweet = kwargs.pop("replied_to", None)
        super(TweetForm, self).__init__(*args, **kwargs)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birthdate', 'city', 'state']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Update My Profile'))


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

class SearchForm(forms.Form):
    query = forms.CharField(max_length=200)
