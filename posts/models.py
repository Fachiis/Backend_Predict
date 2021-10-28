from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=50, help_text="Title of Post")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="posts_likes"
    )

    objects = models.Manager()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail-post", kwargs={"pk": self.pk, })

    def truncate_body(self):
        return self.body[:25]

    def total_likes(self):
        count = self.likes.count()
        return count


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
    value = models.CharField(max_length=6, default="like")

    objects = models.Manager()

    def __str__(self):
        return self.user.username + " - " + self.value
