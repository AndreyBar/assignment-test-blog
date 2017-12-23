from django.conf.urls import url
from django.views.decorators.http import require_POST

from .views import post_list, post_detail, add_comment

urlpatterns = [
	url(r'^$', post_list, name='posts'),	 	# то есть по URL http://имя_сайта/blog/ 
	                                               			# будет выводиться список постов
	url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
	 														# а по URL http://имя_сайта/blog/число/ 
	                                              			# будет выводиться пост с определенным номером
	url(r'^(?P<pk>\d+)/comment/$', add_comment, name='add_comment'),
]