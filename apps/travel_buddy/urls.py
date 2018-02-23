from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^new_trip$', views.new_trip),
    url(r'^destination/(?P<id>\d+)$', views.destination),
    url(r'^join/(?P<id>\d+)$', views.join)
]
