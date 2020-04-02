from django.http import HttpResponse
from django.template import loader

from .models import ActivityEvent


# from django.shortcuts import render

# Create your views here.
def homePageView(request):
    events = ActivityEvent.objects.order_by('-time')
    context = {'events': events}
    template = loader.get_template('tracker/index.html')
    return HttpResponse(template.render(context, request))
