# Create your views here.

from content.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


def home(request):
	return render_to_response("landing.html")

@login_required
def display_all(request):
	pages = Page.objects.all().order_by('order')
	render_to_response("display_all.html", pages)

@login_required
def display_one(request, slug):
	page = Page.objects.filter(slug=slug)[0]
	render_to_response("display_one.html", page)