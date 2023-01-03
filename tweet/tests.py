from django.test import TestCase

# Import your models here
from .models import Tweet, User

class TweetModelTest(TestCase):
    """
    Tests for the Tweet model
    """
    def setUp(self):
        # Create some test data for the Tweet model
        self.user = User.objects.create(username='testuser')
        self.tweet = Tweet.objects.create(user=self.user, content='This is a test tweet')
    
    def test_tweet_creation(self):
        # Test that the tweet was created correctly
        self.assertEqual(self.tweet.content, 'This is a test tweet')
        self.assertEqual(self.tweet.user, self.user)
    
    def test_tweet_str_representation(self):
        # Test the string representation of the tweet
        self.assertEqual(str(self.tweet), 'This is a test tweet')

class UserModelTest(TestCase):
    """
    Tests for the User model
    """
    def setUp(self):
        # Create some test data for the User model
        self.user = User.objects.create(username='testuser')
    
    def test_user_creation(self):
        # Test that the user was created correctly
        self.assertEqual(self.user.username, 'testuser')
    
    def test_user_str_representation(self):
        # Test the string representation of the user
        self.assertEqual(str(self.user), 'testuser')

