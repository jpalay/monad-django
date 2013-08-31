# Create your views here.

from content.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


def home(request):
	return render_to_response("landing.html")

@login_required
def display_all(request):
	pages = Page.objects.all()
	context = {'pages': pages}
	return render_to_response("display_all.html", context)

@login_required
def display_one(request, slug):
	page = Page.objects.get(slug=slug)
	next_page = Page.objects.get(order=page.order + 1)
	previous_page = Page.objects.get(order=page.order - 1)
	context = {
		"page": page,
		"next_page": next_page,
		"previous_page": previous_page,
	}
	return render_to_response("display_one.html", context)