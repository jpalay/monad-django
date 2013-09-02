# Create your views here.

from content.models import *
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def home(request):
    return render_to_response("landing.html")

@login_required
def display_all(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render_to_response("display_all.html", RequestContext(request, context))

@login_required
def display_page(request, slug):
    # if you enter the "order" of the page, it should still work
    page = None
    pages = Page.objects.all()
    if slug.isdigit():
        if slug > 0:
            index = int(slug) - 1
            page = pages[index]
            return redirect('/{0}'.format(page.slug))
    else:
        for i, a_page in enumerate(pages):
            if a_page.slug == slug:
                index = i
                page = a_page
                break
        if page is None:
            return redirect('/')

    
    previous_page = None
    if index > 0:
        try:
            previous_page = pages[index - 1]
        except IndexError, AssertionError:
            previous_page = None

    try:
        next_page = pages[index + 1]
    except IndexError:
        next_page = None

    media = Media.objects.filter(page=page)

    context = {
        "page": page,
        "number": index + 1,
        "next_page": next_page,
        "previous_page": previous_page,
        "media": media,
    }
    return render_to_response("display_one.html", RequestContext(request, context))
