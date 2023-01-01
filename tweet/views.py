from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Tweet, Notification
from .forms import ProfileForm, TweetForm

def home(request):
    tweets = Tweet.objects.all().order_by('-id')
    context = {'tweets': tweets}
    return render(request, 'home.html', context)

def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = TweetForm(user=request.user)
    context = {'form': form}
    return render(request, 'add_tweet.html', context)

def notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False).order_by('-id')
    context = {
        'notifications': notifications,
        'unread_count': notifications.count(),
        'tweets': Tweet.objects.filter(id__in=notifications.values('tweet'))
    }
    return render(request, 'notifications.html', context)

def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user.profile)
    if form.is_valid():
        form.save()
    profile = request.user.profile
    context = {'profile': profile, 'form': form}
    return render(request, 'profile.html', context)

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
