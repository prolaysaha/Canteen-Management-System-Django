from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
 


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    location = models.CharField(max_length=50,default='')
    post = models.CharField(max_length=50,default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])    
        
post_save.connect(create_profile, sender=User)