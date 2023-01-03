from django.contrib import admin
from .models import Profile, Retweet, Hashtag, Tweet, Notification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(Tweet)
admin.site.register(Notification)
admin.site.register(Retweet)
