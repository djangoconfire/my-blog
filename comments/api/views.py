from django.db.models import Q
from rest_framework.generics import \
                ListAPIView,RetrieveAPIView,\
                UpdateAPIView,DestroyAPIView,\
                CreateAPIView,RetrieveUpdateAPIView

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from pagination import PostLimitOffsetPagination,PostPageNumberPagination
from permissions import IsOwnerOrReadOnly
from comments.models import Comment

from serializers import CommentSerializer


class CommentDetailApiView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPiView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['content']
    pagination_class = PostPageNumberPagination

    def get_queryset(self,*args,**kwargs):
        queryset_list=Comment.objects.all()
        query=self.request.GET.get('q')
        if query:
            queryset_list=queryset_list.filter(
                Q(content__icontains=query)
            ).distinct()

        return queryset_list






