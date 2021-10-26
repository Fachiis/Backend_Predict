from django.contrib import admin

from posts.models import Post, Like


class LikeInline(admin.TabularInline):
    model = Like
    extra = 2


class PostAdmin(admin.ModelAdmin):
    inlines = [LikeInline]
    list_display = ['title', 'truncate_body', 'author', 'created_at', ]
    search_fields = ('title', 'author')


admin.site.register(Post, PostAdmin)

