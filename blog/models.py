from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                self).get_queryset()\
                .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )       # creates a drop down list of status choices
    title = models.CharField(max_length=250)        # creates a charater field of title
    slug = models.SlugField(max_length=250,unique_for_date='publish')   #creates a slugfield whichs is what shows in the url
    author = models.ForeignKey(User,related_name='blog_posts')      #creates a foreignkey inheriting from the admin Users
    body = models.TextField()   #creates the body of te field with a textfield
    publish = models.DateTimeField(default=timezone.now)    #creates a datetime field with the default as the current time of creation
    created = models.DateTimeField(auto_now_add=True)   #
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    objects = models.Manager() # The default manager. which is used as model.objects.**** where **** is a attribute which incles gets, filter, order_by, etc
    published = PublishedManager() # Our custom manager. which is used as published.objects.**** inplace of the default manager model.objects.**** where **** is a attribute which incles gets, filter, order_by, etc

    class Meta:
        ordering = ('-publish',)    #this class tells the model to be ordered in descendind order using the publish field


    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                        self.publish.strftime('%m'),
                        self.publish.strftime('%d'),
                        self.slug])

    def __str__(self):
        return self.title
