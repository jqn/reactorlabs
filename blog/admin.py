from django.contrib import admin
from .models import Post, Category
from pagedown.widgets import AdminPagedownWidget
from django.db import models


class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_display = ["title", "last_modified", "created_on"]
    list_display_links = ["last_modified"]
    list_editable = ["title"]
    list_filter = ["last_modified", "created_on"]

    search_fields = ["title", "body"]

    class Meta:
        model = Post


# Register your models here.
admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
