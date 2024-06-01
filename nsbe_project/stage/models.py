from django.db import models

# Create your models here.

class Member(models.Model):
    id_number = models.IntegerField(primary_key=True, editable=True, unique=True, default='000000000')
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    phone = models.IntegerField(default='0000000000')
    major = models.CharField(max_length=50)
    linkedIn = models.URLField(max_length=50, default='http://www.linkedin.com')
    #short_long_term_goals = models.TextField(max_length=1000),
    #contrib_text = models.TextField(max_length=1000)

    def __str__(self):
        return self.fname + " " + self.lname

