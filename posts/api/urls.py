from django.conf.urls import url
from django.contrib import admin

from views import PostListAPiView,PostDetailApiView,PostUpdateApiView,PostDeleteApiView,PostCreateApiView

urlpatterns=[
    url(r'^$',PostListAPiView.as_view(),name='post-list'),
    url(r'^create/$',PostCreateApiView.as_view(),name='post-create'),
    url(r'^(?P<slug>[\w-]+)/$',PostDetailApiView.as_view(),name='post-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$',PostUpdateApiView.as_view(),name='post-update'),
    url(r'^(?P<slug>[\w-]+)/delete/$',PostDeleteApiView.as_view(),name='post-delete'),

]
