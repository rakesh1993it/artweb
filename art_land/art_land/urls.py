from django.conf.urls import patterns, include, url
from art_land import views
from django.contrib import admin
from art_land.forms import ContactForm1, ContactForm2, ContactForm3
from art_land.views import ContactWizard

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'artimages.views.home', name='home'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^artimages/', include('artimages.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^about_us/', views.about_us),
    #url(r'^ratings/', include('ratings.urls')),
    
    # user auth urls
    url(r'^accounts/login/$', views.login),
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid_login/$', views.invalid_login),

    # user registration
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/register_success/$', views.register_success), 
	
    #contact form wizard
    url(r'^contact/$', ContactWizard.as_view([ContactForm1,ContactForm2,ContactForm3])),
)
