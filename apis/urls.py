from django.urls import path

from apis.views import PostList, PostDetail, PostCreate, LikeCreate

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('create-post/', PostCreate.as_view(), name='post-create'),
    path('create-like/<int:pk>/', LikeCreate.as_view(), name='like-update'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
