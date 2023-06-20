from django.db import models
from mdeditor.fields import MDTextField

class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    content = MDTextField()
    tags = TaggableManager()
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.slug

    def __repr__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.generate_meta_title()
        if not self.meta_description:
            self.meta_description = self.generate_meta_description()
        super(Post, self).save(*args, **kwargs)

    def generate_meta_title(self):
        # Customize this method to generate an effective meta title
        # based on the post's title or any other relevant information.
        return f"{self.title} - Your Website Name"

    def generate_meta_description(self):
        # Customize this method to generate an effective meta description
        # based on the post's content or any other relevant information.
        return f"A brief description of the post: {self.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default='...')

    def __str__(self):
        return f'{self.content[:20]}...-{self.author}-{self.post}'
