from rest_framework import viewsets

from .models import Post, Author, Comment
from .serializers import PostSerializer, AuthorSerializer
from .serializers import CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    fields_choices = dict(
        {
            'authors': {
                'source': 'author',
                'many': True
            },
            'comments': {
                'source': 'comment',
                'many': True
            }
        }
    )


class AuthorViewSet(viewsets.ModelViewSet):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    fields_choices = dict(
        {
            'posts': {
                'source': 'post',
                'many': True
            }
        }
    )


class CommentViewSet(viewsets.ModelViewSet):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
