from rest_framework import serializers

from posts.models import Post, PostImage


class FilterIsNotPostedListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(post__isnull=True)
        return super(FilterIsNotPostedListSerializer, self).to_representation(data)


class PostImageSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.ReadOnlyField(source="post.pid")

    class Meta:
        model = PostImage
        fields = ["url", "id", "name", "post", "thumb", "large", "position"]


class ShortPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "position", "name", "thumb", "large"]
        list_serializer_class = FilterIsNotPostedListSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    images = ShortPostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = ["url", "id", "posted_by", "name", "text", "images"]

    def create(self, validated_data):
        images_data = validated_data.pop("images")
        tweet = Post.objects.create(**validated_data)
        for pos, image_data in enumerate(images_data):
            PostImage.objects.create(tweet=tweet, **image_data, position=pos + 1)
        return tweet


class ShortPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "text",
        ]
