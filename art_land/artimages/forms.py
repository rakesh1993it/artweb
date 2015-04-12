from django import forms
from models import Article, Comment, BuyArticle 

class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article 
		fields = ('title','picture','body','pub_date')

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('name', 'body' )

class BuyArticleForm(forms.ModelForm):
	class Meta:
		model = BuyArticle
		fields = ('Name', 'Address','Mobile_No', 'Atmcard', 'Cash_on_delevary')
