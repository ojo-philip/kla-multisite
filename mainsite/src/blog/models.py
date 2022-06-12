from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now=False, auto_now_add=False)
  content = RichTextUploadingField()
  author = author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  image = models.ImageField( upload_to="post-image")
  slug = models.SlugField(max_length=200, default='', editable=False)

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return self.title

  def get_absolute_url(self):
        kwargs = {
            "pk": self.id,
            'slug': self.slug,
        }
        return reverse("blog:post_detail", kwargs=kwargs)

  def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

