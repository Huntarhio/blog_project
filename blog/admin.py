from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')   #specifies the model field we want to see in our admin pages
    list_filter = ('status', 'created', 'publish', 'author')    # specifies how the items in the admin page should be filtered
    search_fields = ('title', 'body')   #creates a search field and specifies which field of the model to be searches
    prepopulated_fields = {'slug': ('title',)}  #   automatically populates the slug field using the title field
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'  #create a date heirachy that the model tries to filter
    ordering = ['status', 'publish']    #ordering the tanle based on status and publsh fied

admin.site.register(Post, PostAdmin)    #registering the Post model inheriting from he PostAdmin class
