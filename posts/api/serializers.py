from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'title',
            'content'
        ]


post_detail_url=HyperlinkedIdentityField(
    view_name='posts-api:post-detail',
    lookup_field='slug'
)

class PostListSerializer(ModelSerializer):
    url=post_detail_url
    class Meta:
        model=Post
        fields=[
            'url',
            'user',
            'title',
            'slug',
            'content'
        ]



class PostDetailSerializer(ModelSerializer):
    url=post_detail_url
    image=SerializerMethodField()
    html=SerializerMethodField()
    class Meta:
        model=Post
        fields=[
            'url',
            'id',
            'user',
            'title',
            'slug',
            'image',
            'html',
            'content'
        ]

    def get_html(self,obj):
        return obj.get_markdown()

    def get_image(self,obj):
        try:
            image=obj.image.url
        except:
            image=None
        return image