from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "num_posts"]


admin.site.register(Tag, TagAdmin)
