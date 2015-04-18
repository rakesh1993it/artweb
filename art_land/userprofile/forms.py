from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('likes_art', 'favorite_art', 'address','mobile_no', 'about_you')