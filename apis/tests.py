import json

from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post
from apis.serializers import PostSerializer

# initialize the APIClient app
client = Client()

# Initialize the User app
User = get_user_model()


class GetAllPostsAPITest(TestCase):
    """ Test module for GET all posts API """

    def setUp(self):
        self.test_user = User.objects.create_user(
            username="fachiis",
            password="1234",
        )

        self.test_user1 = User.objects.create_user(
            username="felix",
            password="1234",
        )

        self.test_post = Post.objects.create(
            author=self.test_user,
            title="Grace",
            body="Yes, it is by His Grace alone",
        )
        self.test_post1 = Post.objects.create(
            author=self.test_user1,
            title="Mercy",
            body="Yes, it is by His Mercy alone",
        )

    def test_get_all_posts(self):
        # Get API response
        response = client.get(reverse('post-list'))
        # Get data from db
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePostTest(TestCase):
    """ Test module for GET single post API """

    def setUp(self):
        self.test_user = User.objects.create_user(
            username="fachiis",
            password="1234",
        )

        self.test_user1 = User.objects.create_user(
            username="felix",
            password="1234",
        )

        self.test_post = Post.objects.create(
            author=self.test_user,
            title="Grace",
            body="Yes, it is by His Grace alone",
        )
        self.test_post1 = Post.objects.create(
            author=self.test_user1,
            title="Mercy",
            body="Yes, it is by His Mercy alone",
        )

    def test_get_valid_single_post(self):
        # get API response
        response = client.get(reverse('post-detail', kwargs={'pk': self.test_post.pk}))

        # Get data from db
        post = Post.objects.get(pk=self.test_post.pk)
        serializer = PostSerializer(post)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_post(self):
        response = client.get(
            reverse('post-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPostTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.test_user = User.objects.create_user(
            username="fachiis",
            password="1234",
        )

        self.test_user1 = User.objects.create_user(
            username="felix",
            password="1234",
        )

        self.valid_post = {
            'author': "self.test_user",
            'title': "Mercy",
            'body': "Yes, it is by His Mercy alone",
        }
        self.invalid_post = {
            'author': self.test_user1,
            'title': 'Grace',
            'body': '',
        }

    def test_create_valid_post(self):
        response = client.post(
            reverse('post-create'),
            data=json.dumps(self.valid_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_post(self):
        response = client.post(
            reverse('post-create'),
            data=json.dumps(self.invalid_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
