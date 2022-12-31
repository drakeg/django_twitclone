from django.contrib import admin
from .models import Profile, Hashtag, Tweet

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(Tweet)
