from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.page_list, name='page_list'),
    url(r'^station/(?P<pk>[0-9]+)/$', views.page_metro, name='page_metro'),
    url(r'^bars/(?P<pk>[0-9]+)/$', views.page_bar, name='page_bar'),
    url(r'^result/$', views.bar_view, name='bar_view')
]