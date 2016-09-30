from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calc_hit/$', views.calc_hit, name='calc_hit'),
]
