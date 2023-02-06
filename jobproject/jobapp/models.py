from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    # email=models.EmailField()
    def __str__(self):
        return self.user.username

    # def __str__(self):
    #     return self.user.email


class userr(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=10)


class postjob(models.Model):
    exp=[
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10'),
    ]
    catchoice=[
        ('remote','remote'),
        ('hybrid','hybrid')
    ]
    jobtype=[
        ('partime','partime'),
        ('fulltime','fulltime'),
    ]
    title=models.CharField(max_length=20)
    cname=models.CharField(max_length=20)
    cemail=models.EmailField()
    expe=models.CharField(max_length=10,choices=exp)
    wplace=models.CharField(max_length=20,choices=catchoice)
    emp=models.CharField(max_length=20,choices=jobtype)


class applyjobmodel(models.Model):
    relocate=[
        ('yes','yes'),
        ('no','no')
    ]

    fullname=models.CharField(max_length=30)
    jobtitle=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    qualification=models.CharField(max_length=150)
    passingyear=models.IntegerField()
    skills=models.CharField(max_length=300)
    relocate=models.CharField(max_length=30,choices=relocate)
    pdone=models.CharField(max_length=800)
    resume=models.FileField(upload_to='jobapp/static')
    companyname=models.CharField(max_length=50)