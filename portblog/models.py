from ipaddress import ip_address
from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=40)
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class comment(models.Model):
    blog = models.ForeignKey(post, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=40)
    email = models.EmailField()
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.commenter

# class globalLoggingData(models.Model):
#     vists = models.IntegerField(default=0)

# class visitorLoggingData(models.Model):
#     ip_address = models.IPAddressField()
    

