from django.contrib import admin
from .models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',
                    'status', 'category')   #specifies the model field we want to see in our admin pages
    list_filter = ('status', 'created', 'publish', 'author', 'category')    # specifies how the items in the admin page should be filtered
    search_fields = ('title', 'body')   #creates a search field and specifies which field of the model to be searches
    prepopulated_fields = {'slug': ('title',)}  #   automatically populates the slug field using the title field
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'  #create a date heirachy that the model tries to filter
    ordering = ['status', 'publish']    #ordering the tanle based on status and publsh fied

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)    #registering the Post model inheriting from the PostAdmin class
admin.site.register(Comment, CommentAdmin) #registering the Comment model inheriting from the CommentAdmin class
