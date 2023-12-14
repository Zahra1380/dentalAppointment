from django.db import models
from account.models import User
from django.utils.html import mark_safe
from account.models import User
# Create your models here.

class BlogModel(models.Model):
    photo = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    publish_date = models.DateField(auto_now=True)
    text = models.TextField()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.photo))

    image_tag.short_description = 'Image'
    def __str__(self):
        return self.title

class Visitors(models.Model):
    visitors = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visit')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='visited')

    def __str__(self):
        return self.visitors.name + ' - ' + self.visitors.last_name + ': ' + self.blog.title