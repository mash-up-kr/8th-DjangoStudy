from django.contrib import admin

from .models import Post, Comment, DjangoStudyMember


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(DjangoStudyMember)
class DjangoStudyMemberAdmin(admin.ModelAdmin):
    pass
