from rest_framework import routers
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from webapp.views import InformationView
from webapp.views import CodeView
from webapp.views import TextView
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
helper_patterns = [
    url('admin/', admin.site.urls),
    url('api/information/',InformationView.as_view(),name='getinformation'),
    url(r'^api/text/(?P<length>[0-9]+)/',TextView.as_view(),name='gettext'),
   # path('api/music/(?P<length>[0-9]+)$/',),
    url(r'^api/code/(?P<length>[0-9]+)/$',CodeView.as_view(),name='getcode')

]
urlpatterns=helper_patterns
