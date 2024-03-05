from django.contrib import admin
from posts.models import Post, PostImage


class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "posted_by", "num_images"]
    list_filter = ["posted_by"]
    search_fields = ("id",)

    inlines = [PostImageInline]

    def num_images(self, obj):
        return len(obj.images.all())

    num_images.short_description = "images"


class PostImageAdmin(admin.ModelAdmin):
    list_display = ["id", "post_id", "position", "name"]
    search_fields = ("id",)

    def post_id(self, obj):
        return obj.post.id

    post_id.short_description = "post"


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
