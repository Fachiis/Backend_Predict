from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, LikeSerializer
from posts.models import Post, Like


class PostCreate(generics.CreateAPIView):
    """Create a post object (POST method)"""
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Fetch the current logged in user and pass it to the author field of the Post"""
        user = self.request.user
        serializer.save(author=user)


class PostList(APIView):
    """Get all posts objects (GET method)"""
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Get a single post object, update or delete the object (GET{id}, PUT, PATCH, DELETE)"""
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class LikeCreate(APIView):
    """Create a like on a single post object, check if user has already liked else pass in user"""
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikeSerializer

    def post(self, request, pk):
        user = self.request.user
        post = Post.objects.get(pk=pk)
        check_like = Like.objects.filter(user=user, post=post)
        if check_like.exists():
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "You have already liked the post"
            })
        post.likes.add(user)
        new_like = Like.objects.create(user=user, post=post)
        new_like.save()
        serializer = LikeSerializer(new_like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
