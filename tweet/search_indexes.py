from haystack import indexes
from tweet.models import Hashtag, Tweet

class TweetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    created_at = indexes.DateTimeField(model_attr='created_at')

    def get_model(self):
        return Tweet

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class HashtagIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Hashtag
