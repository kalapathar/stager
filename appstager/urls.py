from django.conf.urls import url

from . import views

app_name = 'appstager'

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^index/', views.index, name='index'),
    url(r'^(?P<show_id>[0-9]+)/$', views.showActions, name='showActions'),
    url(r'^choice/',views.choice,name='choice'),
    url(r'^addshow/',views.show,name='show'),
	# AJAX URLs
	url(r'^getAction$', views.getAction, name='getAction'),
	url(r'^createAction/(?P<actType>[\w]+)$', views.createAction, name='createAction'),
	url(r'^updateActionUp/(?P<order>[\w]+)$', views.updateActionUp, name='updateActionUp'),
	url(r'^updateActionDown/(?P<order>[\w]+)$', views.updateActionDown, name='updateActionDown'),
	url(r'^activeAction/(?P<name>[\w]+)$', views.activeAction, name='activeAction'),
	url(r'^submitAction$', views.submitAction, name='submitAction')
]
