from django.urls import path
from posts.views import PostDetail, PostImageDetail, PostImageList, PostList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("", PostList.as_view(), name="post-list"),
    path("<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("images/", PostImageList.as_view(), name="postimage-list"),
    path("images/<int:pk>/", PostImageDetail.as_view(), name="postimage-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
