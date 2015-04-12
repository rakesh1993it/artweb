from django.db import models
#from djangorating.fields import RatingField
from django.contrib.auth.models import User
from time import time
#import os.path
#rom art_land import settings




def get_upload_file_name(instance, filename):
	return "images/%s_%s" % (str(time()).replace('.','_'), filename)


class Article(models.Model):
	user = models.ForeignKey(User, null=True)
	title = models.CharField(max_length=200)
	picture = models.FileField(upload_to= get_upload_file_name, blank=True, null=True)
	body = models.TextField()
	pub_date = models.DateTimeField('date_published', null=True)
	likes = models.IntegerField(default=0)
	ratings = models.IntegerField(default=0, null=True)
	
	def __unicode__(self):
		return self.title
   
	def get_absolute_url(self):
		return "/artimages/get/%i/" % self.id

	

class Comment(models.Model):
	article = models.ForeignKey(Article)
	name = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date_published', null=True)
 
#class RatingArticle(models.Model):
#	user = models.ForeignKey(User)
#	article = models.ForeignKey(Article)
#	rating = models.IntegerField(default=0)
	
class BuyArticle(models.Model):
	article = models.ForeignKey(Article)
	Name = models.CharField(max_length=200)
	Address = models.CharField(max_length=500)
	Atmcard = models.BooleanField(default=False)
	Mobile_No = models.CharField(max_length=20)
	Cash_on_delevary = models.BooleanField(default=False)
	Date = models.DateTimeField(auto_now_add=True, null=True)
 
	