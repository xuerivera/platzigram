"""Platzigram Views"""
# Django
from django.http import HttpResponse, JsonResponse
# Misc
from datetime import datetime


def hello_world(request):
    return HttpResponse('Hello World! the current time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))

def sort_int(request):
    """returns a jasonresponse with sorted numbers"""
    number = sorted(request.GET['numbers'].split(','))[0:]
    response = JsonResponse({
        'message': 'Hi {number}'.format(number=number)
    })
    return response
   
def say_hi(request, name, age):
    """returns a jasonresponse with a message"""
    if age < 18:
        message = 'Sorry {}, you are not old enough'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)
    return JsonResponse({
        'message': message
    })