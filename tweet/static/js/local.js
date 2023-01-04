$('.like-button').click(function() {
  var tweetId = $(this).data('tweet-id');
  $.ajax({
    url: '/like/',
    data: {
      'tweet_id': tweetId
    },
    dataType: 'json',
    success: function(data) {
      console.log(data);
    }
  });
});
