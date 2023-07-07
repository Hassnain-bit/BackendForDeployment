from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class History(models.Model):
    userid= models.ForeignKey(User,on_delete=models.CASCADE)
    keyword= models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword


