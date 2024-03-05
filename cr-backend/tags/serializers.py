from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    num_posts = serializers.ReadOnlyField()

    class Meta:
        model = Tag
        fields = ["name", "num_posts"]
