from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'stage/index.html')


def about(request):
    return render(request, 'stage/about.html')

def directory(request):
    return render(request, 'stage/directory.html')

def events(request):
    return render(request, 'stage/events.html')

def help(request):
    return render(request, 'stage/help.html')

def points(request):
    return render(request, 'stage/points.html')

def profile(request):
    return render(request, 'stage/profile.html')