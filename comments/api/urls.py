from django.conf.urls import url
from django.contrib import admin

from views import CommentListAPiView,CommentDetailApiView

urlpatterns=[
    url(r'^$',CommentListAPiView.as_view(),name='comment-list'),
    url(r'^(?P<id>\d+)/$',CommentDetailApiView.as_view(),name='comment-detail'),


]
