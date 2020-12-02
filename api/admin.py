from django.contrib import admin
from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'following')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
