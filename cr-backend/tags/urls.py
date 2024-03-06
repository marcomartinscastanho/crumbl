from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("tags/", views.TagList.as_view(), name="tag-list"),
    path("tags/<int:pk>/", views.TagDetail.as_view(), name="tag-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
