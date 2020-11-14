from dcx_django.helpers import DcxModelSerializer
from .models import Post, Author, Comment


class PostSerializer(DcxModelSerializer):
    class Meta:
        model = Post
        fields = ['url', 'title', 'authors', 'content', 'comments']
        related_fields = ['authors', 'comments']


class AuthorSerializer(DcxModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'name', 'email', 'posts']
        related_fields = ['posts']


class CommentSerializer(DcxModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'reader_name', 'comment', 'post']
        related_fields = ['post']

