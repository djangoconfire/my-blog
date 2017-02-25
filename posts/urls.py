from django.conf.urls import url, include
from views import post_list,post_create,post_delete,post_detail,post_update

urlpatterns=[

    # post-list
    url(r'^$',post_list,name="post-list"),
    # post-create
    url(r'^create/$',post_create,name="post-create"),
    #post-detail
    url(r'^(?P<slug>[\w-]+)/$',post_detail,name="post-detail"),
    #post-delete
    url(r'^(?P<slug>[\w-]+)/delete/$',post_delete,name="post-delete"),
    #post-update
    url(r'^(?P<slug>[\w-]+)/edit/$',post_update,name="post-update"),


]