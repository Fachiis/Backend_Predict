from django.contrib import admin

from posts.models import Post, Like


class LikeInline(admin.TabularInline):
    """The admin interface will have the ability to edit both Post and Like models on the same page as a parent
    model. """
    model = Like
    extra = 2


class PostAdmin(admin.ModelAdmin):
    """The parent model admin"""
    inlines = [LikeInline]
    list_display = ['title', 'truncate_body', 'author', 'created_at', ]
    search_fields = ('title', 'author')


admin.site.register(Post, PostAdmin)

