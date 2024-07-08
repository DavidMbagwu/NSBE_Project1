from django.shortcuts import render
from .models import Member
from .models import Post

# Create your views here.
def index(request):
    all_users = Member.objects.all()
    return render(request, 'stage/index.html', {'all': all_users})


def about(request):
    return render(request, 'stage/about.html')

def directory(request):
    return render(request, 'stage/directory.html')

def events(request):
    return render(request, 'stage/events.html')

def help(request):
    return render(request, 'stage/help.html')

def points(request):
    context = {
        'posts': Post.objects.all(),
        'members': Member.objects.all(),
    }
    return render(request, 'stage/points.html', context)

def profile(request):
    all_users = Member.objects.all()
    return render(request, 'stage/profile.html', {'all': all_users})

def login(request):
    return render(request, 'stage/login.html')

def signup(request):
    return render(request, 'stage/signup.html')

def gallery(request):
    return render(request, 'stage/gallery.html')

def adminOnly(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'stage/adminOnly.html', context)