from django.db import models


# ## Models

class Post(models.Model):
    title = models.CharField(max_length=255, help_text='Blog Post Title')
    content = models.TextField(help_text='Blog Post Content')
    authors = models.ManyToManyField('Author', related_name='posts')
    # Have a one-to-many relationship with Comment, see post field
    # in Comment model


class Author(models.Model):
    name = models.CharField(max_length=255, help_text='Author Name')
    email = models.CharField(max_length=255, help_text='Author E-mail')


class Comment(models.Model):
    reader_name = models.TextField(help_text='Reader Name')
    comment = models.TextField(help_text='Reader Comment')
    post = models.ForeignKey(Post, models.CASCADE, related_name='comments')
