from django import forms
from .models import Profile, Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields['user_id'] = forms.CharField(widget=forms.HiddenInput(), initial=user.id)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birthdate', 'city', 'state']

