from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.utils import timezone 
from django.contrib.auth.models import User
from artimages.models import Article,Comment, BuyArticle #RatingArticle
from forms import ArticleForm, CommentForm,BuyArticleForm #RatingArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages
#from haystack.query import SearchQuerySet 

# Create your views here.

def articles(request):
	language = 'en_us'
	session_language = 'en_us'

	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']
	
	args = {}
	args.update(csrf(request))
	
	args['articles'] = Article.objects.all()
	args['language'] = language
	args['session_language'] = session_language
	#paginate_by = 4

	return render_to_response("articles.html", args)
								
def article(request, article_id=1):
	#return render_to_response("article.html",
	#				{'article': Article.objects.get(id=article_id)})
	return render(request, "article.html",
					{'article': Article.objects.get(id=article_id)})



def language(request, language='en_us'):
	response = HttpResponse('setting language to %s' % language)

	response.set_cookie('lang', language)
	request.session['lang'] = language
	return response

@login_required
def create(request):
	if request.POST:
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			
			messages.add_message(request, messages.SUCCESS, ' your article was added')
			return HttpResponseRedirect('/artimages/all')
	else:
		form = ArticleForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('create_article.html', args)

@login_required
def like_article(request, article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()
	return HttpResponseRedirect('/artimages/get/%s' % article_id)

def rating_article(request, article_id):
	#a = Article.objects.get(id=article_id)
	if request.method == "POST":
		a = Article.objects.get(id=article_id)
		#form = RatingArticleForm(request.POST)
		#if form.is_valid():
		#	c = f.save(commit=False)

		sums += a.ratings
		count += 1
		rate = float(sums/count)
		a.ratings = rate
		a.save()

	return HttpResponseRedirect('/artimages/get/%s' % article_id)

	
	


@login_required
def add_comment(request, article_id):
	a = Article.objects.get(id=article_id)
	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.article = a
			c.save()

		messages.success (request, 'your Coment was added')
		return HttpResponseRedirect('/artimages/get/%s' % article_id)

	else:
		f = CommentForm()
	args = {}
	args.update(csrf(request))
	args['article'] = a
	args['form'] = f
	return render_to_response('add_comment.html', args) 



def search_titles(request):
	if request.method == "POST":
		search_text = request.POST['search_text']
	else:
		search_text = ''
	articles = Article.objects.filter(title__contains=search_text)	
	return render_to_response('ajax_search.html',{'articles' : articles})

@login_required
def buy_article(request, article_id):
	a = Article.objects.get(id=article_id)
	if request.method == "POST":
		f = BuyArticleForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.article = a
			c.save()

		messages.success (request, 'your are successful bought this Art')
		return HttpResponseRedirect('/artimages/get/%s' % article_id)

	else:
		f = BuyArticleForm
	args = {}
	args.update(csrf(request))
	args['article'] = a
	args['form'] = f
	return render_to_response('buy_article.html', args) 



def home(request):

	args = {}
	args.update(csrf(request))
	
	args['articles'] = Article.objects.all()
	#args['language'] = language
	#args['session_language'] = session_language
	#paginate_by = 4
	return render_to_response("home.html", args)




