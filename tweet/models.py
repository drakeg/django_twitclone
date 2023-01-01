from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
import re

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = USStateField(blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    def __str__(self):
        return self.user.username

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='tweet_images', blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    replied_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Find @username patterns in the tweet content
        pattern = r'@(?P<username>\w+)'
        mentions = re.finditer(pattern, self.content)
        # Create notifications for each mentioned user
        for mention in mentions:
            username = mention.group('username')
            try:
                mentioned_user = User.objects.get(username=username)
                notification = Notification(user=mentioned_user, message=f'You were mentioned in a tweet by {self.user.username}')
                notification.save()
            except User.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.content

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

class Hashtag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
