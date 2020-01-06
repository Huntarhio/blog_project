from django.contrib.sitemaps import Sitemap
from .models import Post
class PostSitemap(Sitemap):
    changefreq = 'weekly'   #defines how frequent changes are made to the site
    priority = 0.9      #defines how important the site is

    def items(self):
        """
        description: gets all the publihed posts
        """
        return Post.published.all()
    def lastmod(self, obj):
        """
        description: gets the last time the post was modified which is set to be the published date
        """
        return obj.publish
