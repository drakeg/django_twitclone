from django.contrib import admin
from .models import Like, Profile, Hashtag, Tweet, Notification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(Tweet)
admin.site.register(Notification)
admin.site.register(Like)
