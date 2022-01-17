from django.contrib import admin
from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'profile', )
    list_filter = ('title', 'modified', 'created' )
    ordering = ('profile', 'user')
    list_display_links = ('title', 'user')


    