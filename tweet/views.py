from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Tweet, Notification, Profile, Hashtag
from .forms import ProfileForm, TweetForm, RegistrationForm, SearchForm
from django.contrib.auth.models import User
from django.contrib import messages
import re

def home(request):
    tweets = Tweet.objects.all().order_by('-id')
    search_form = SearchForm()
    context = {'tweets': tweets, 'search_form': search_form}
    return render(request, 'home.html', context)

def add_tweet(request, replied_to=None):
    replied_to_tweet = None
    if replied_to and Tweet.objects.filter(pk=replied_to).exists():
        replied_to_tweet = Tweet.objects.get(pk=replied_to)
    print(replied_to_tweet)

    # If the request method is POST, process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = TweetForm(request.POST, request=request, replied_to=replied_to_tweet)

        # Check if the form is valid
        if form.is_valid():
            # Save the tweet to the database
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.replied_to = replied_to_tweet
            tweet.save()

            # Notify the original tweet author if this is a reply
            if replied_to_tweet and replied_to_tweet.user != request.user:
                notification = Notification(message=tweet, user=replied_to_tweet.user)
                notification.save()


            # Extract hashtags from the tweet text
            hashtags = re.findall(r'#(\w+)', tweet.content)
            for hashtag in hashtags:
                # Create a Hashtag object, or retrieve an existing one
                obj, created = Hashtag.objects.get_or_create(name=hashtag)
                # Add the hashtag to the tweet
                tweet.hashtags.add(obj)

            # Redirect to the home page
            messages.success(request, 'Your tweet has been added')
            return redirect('home')

    # If the request method is GET (or any other method), create a blank form
    else:
        form = TweetForm(request=request, replied_to=replied_to_tweet)

    # Render the template with the form
    return render(request, 'add_tweet.html', {'form': form, 'replied_to': replied_to_tweet})

def notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False).order_by('-id')
    context = {
        'notifications': notifications,
        'unread_count': notifications.count(),
    }
    return render(request, 'notifications.html', context)

def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user.profile)
    if form.is_valid():
        form.save()
    profile = request.user.profile
    context = {'profile': profile, 'form': form}
    return render(request, 'profile.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile(user=user)
            profile.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def search(request):
    tweets = []
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets = Tweet.objects.filter(content__icontains=query)
    return render(request, 'search.html', {'form': form, 'tweets': tweets})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message
            pass
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
