from rest_framework import serializers

from posts.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'total_likes', 'created_at', 'updated_at', ]


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.title')
    value = serializers.ReadOnlyField()

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'value', ]
