from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path
from core.views import view1, home, get_bot_response
from django.urls import re_path


urlpatterns = [
    path('abc/', view1),
    path('', home),
    path('get/', get_bot_response),
]
