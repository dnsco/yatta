from django.shortcuts import render
from .models import ActivityEvent

def homePageView(request):
    events = ActivityEvent.objects.order_by('-time')
    context = {'events': events}
    return render(request, 'tracker/index.html', context)
