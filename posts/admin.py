from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','updated', 'timestamp',)
    list_display_links = ["updated"]
    list_filter = ['updated','timestamp']
    search_fields = ['title','content']
    class Meta: #his is just a class container with some options (metadata) attached to the model.
        model = Post


admin.site.register(Post, PostModelAdmin)
