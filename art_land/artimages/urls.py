from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from artimages import views

urlpatterns = patterns('',

    # Examples:
    url(r'^all/$', views.articles),
    url(r'^get/(?P<article_id>\d+)/$', views.article),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    url(r'^create/$', views.create),
    url(r'^like/(?P<article_id>\d+)/$', views.like_article),
    url(r'^add_comment/(?P<article_id>\d+)/$', views.add_comment),
    url(r'^search/$', views.search_titles),
    url(r'^buy_article/(?P<article_id>\d+)/$', views.buy_article),
    url(r'^rating/(?P<article_id>\d+)/$', views.rating_article),
    # url(r'^blog/', include('blog.urls')),
  ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
