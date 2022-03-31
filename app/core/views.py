import logging
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


logger = logging.getLogger('main')

@csrf_exempt
def view1(request):
    logger.info('hello')
    return HttpResponse('Hi There')