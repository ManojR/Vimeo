# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from appvimeo.models import search_posts
from django.template.loader import get_template
from django.template import Context


def home(request):

    
    if 'q' in request.GET and request.GET['q']:
        message = 'You searched for: %r' % request.GET['q']
    else:
        messge = 'you submitted an empty form'    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        entry = search_posts.objects.filter(name__icontains=q)

    return render_to_response('searchvimeo.html',locals())


