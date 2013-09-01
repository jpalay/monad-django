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
def display_page(request, slug):
	# if you enter the "order" of the page, it should still work
	pages = Page.objects.all()
	if slug.isdigit():
		if slug > 0:
			index = int(slug) - 1
			page = pages[index]
	else:
		for i, a_page in enumerate(pages):
			if a_page.slug == slug:
				index = i
				page = a_page
				break
	try:
		next_page = page[index + 1]
	except IndexError:
		next_page = None

	try:
		previous_page = page[index - 1]
	except IndexError:
		previous_page = None

	context = {
		"page": page,
		"next_page": next_page,
		"previous_page": previous_page,
	}
	return render_to_response("display_one.html", context)
