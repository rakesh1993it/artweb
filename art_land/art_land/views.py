from django.shortcuts import render, render_to_response 
from django.http import HttpResponseRedirect
#from .import models
from django.contrib import auth
from django.core.context_processors import csrf
from forms import SignUpForm
#from forms import ContactForm
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
import logging
logr = logging.getLogger(__name__)
								


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST or None)

		if form.is_valid():
			#save_it = form.save(commit=False)
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))
	args['form'] = SignUpForm()

	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')


	

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response("login.html", c)

def auth_view(request):
	username = request.POST.get("username", "")
	password = request.POST.get("password", "")
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect("/accounts/loggedin")
	
	else:
		return HttpResponseRedirect("/accounts/invalid_login")

def loggedin(request):
	return render_to_response("loggedin.html",
								{"first_name": request.user.first_name})

def invalid_login(request):
	return render_to_response("invalid_login.html")

def logout(request):
	auth.logout(request)
	return render_to_response("logout.html")


class ContactWizard(SessionWizardView):
	template_name = "contact_form.html"

	def done(self, form_list, **kwargs):
		form_data = process_form_data(form_list)

		return render_to_response('done.html', {'form_data' : form_data})

def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]

	logr.debug(form_data[0]['subject'])
	logr.debug(form_data[1]['sender'])
	logr.debug(form_data[2]['message'])

	#-------- only use if an SMTP server is setup --------#
	send_mail(form_data[0]['subject'],
			  form_data[1]['sender'], form_data[2]['message'],
	 		  ['rakesh190493it@gmail.com'], fail_silently=False)
	
	return form_data

def about_us(request):
	return render_to_response('about_us.html')

