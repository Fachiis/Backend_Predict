from django.conf import settings
from django.db import models

LIKES = [
    ('like', 'like'),
    ('unlike', 'unlike')
]


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="posts_likes",
    )
    title = models.CharField(max_length=50, help_text="Title of Post")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.liked.all().count()

    def truncate_body(self):
        return self.body[:25]


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="posts_likes"
    )
    value = models.CharField(choices=LIKES, max_length=6)

    objects = models.Manager()

    def __str__(self):
        return self.user.username + " - " + self.value
