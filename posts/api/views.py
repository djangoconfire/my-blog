from django.db.models import Q
from rest_framework.generics import \
                ListAPIView,RetrieveAPIView,\
                UpdateAPIView,DestroyAPIView,\
                CreateAPIView,RetrieveUpdateAPIView

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from pagination import PostLimitOffsetPagination,PostPageNumberPagination
from permissions import IsOwnerOrReadOnly
from posts.models import Post

from serializers import PostListSerializer,PostDetailSerializer,PostCreateUpdateSerializer

class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostListAPiView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields=['title','content']
    pagination_class = PostPageNumberPagination

    def get_queryset(self,*args,**kwargs):
        queryset_list=Post.objects.all()
        query=self.request.GET.get('q')
        if query:
            queryset_list=queryset_list.filter(
                Q(title__icontains=query),
                Q(content__icontains=query)
            ).distinct()

        return queryset_list

class PostRetrieveUpdateApiView(RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'

    def perform_update(self,serializer):
        serializer.save(user=self.request.user)


class PostUpdateApiView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly,IsOwnerOrReadOnly]





