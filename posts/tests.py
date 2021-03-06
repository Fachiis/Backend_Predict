from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post

# initialize the User app
User = get_user_model()


class PostTest(TestCase):
    """Test the posts app"""
    def setUp(self):
        """The set up test data for the post test using class method instead of object methods"""
        # Create a user
        self.test_user = User.objects.create_user(
            username="fachiis",
            password="1234"
        )

        # Create a post
        self.test_post = Post.objects.create(
            author=self.test_user,
            title="Grace",
            body="Yes, it is by His Grace alone",
        )

    def test_post_content(self):
        """Test the post content"""
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, "fachiis")
        self.assertEqual(title, "Grace")
        self.assertEqual(body, "Yes, it is by His Grace alone")
