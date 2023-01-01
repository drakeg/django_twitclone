from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields['user_id'] = forms.CharField(widget=forms.HiddenInput(), initial=user.id)

