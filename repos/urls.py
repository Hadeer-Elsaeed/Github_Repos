from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('languages', views.p_languages, name='p_languages'),
    path('languages/<language>', views.info_languages, name='info_languages')
]