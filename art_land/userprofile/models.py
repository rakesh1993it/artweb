from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	likes_art = models.BooleanField(default=False)
	favorite_art = models.CharField(max_length=200, null= True)
	address = models.CharField( max_length=500, null=True)
	mobile_no = models.CharField(max_length=30, null=True)
	about_you = models.TextField(null=True)
	

# if object exists grab it, else create it
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


