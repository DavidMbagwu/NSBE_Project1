from django.db import models
from django.utils import timezone
# Create your models here.

class Member(models.Model):
    id_number = models.IntegerField(primary_key=True, editable=True, unique=True, default='000000000')
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.IntegerField(blank = True)
    major = models.CharField(max_length=50)
    linkedIn = models.URLField(max_length=50, default='http://www.linkedin.com')
    pointsum = models.IntegerField(blank = True)
    #short_long_term_goals = models.TextField(max_length=1000),
    #contrib_text = models.TextField(max_length=1000)

    def __str__(self):
        return self.fname + " " + self.lname

class Post(models.Model):
    member = models.ManyToManyField(Member, related_name= 'points')
    event = models.CharField(max_length = 100)
    description = models.TextField()
    points = models.IntegerField()
    date_event = models.DateField(default = timezone.now)


    def __str__(self):
        return self.event