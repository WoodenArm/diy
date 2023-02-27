from django.contrib import admin
from .models import Posts, Photos, Comments
from django.utils.safestring import mark_safe

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'is_published', 'post_id')
    list_display_links = ('title', 'get_html_photo')
    prepopulated_fields = {'slug': ('title',)}

    def get_html_photo(sefl, object):
        return mark_safe(f"<img src='{object.image.url}' width=50>")

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'time_create', 'owner')
    list_display_link = ('id', 'owner')
    prepopulated_fields = {'slug': ('text',)}

admin.site.register(Posts, PostsAdmin)
admin.site.register(Photos, PhotoAdmin)
admin.site.register(Comments, CommentAdmin)


