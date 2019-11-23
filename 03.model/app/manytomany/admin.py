from django.contrib import admin

from .models import (
    InstagramPost,
    HashTag,
    InstagramUser,
    InstagramPostLike,
    FacebookUser,
    TwitterUser, GitHubUser, GitHubRelation)


@admin.register(InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    pass


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass


@admin.register(InstagramPostLike)
class InstagramPostLikeAdmin(admin.ModelAdmin):
    pass


@admin.register(InstagramUser)
class InstagramUserAdmin(admin.ModelAdmin):
    pass


@admin.register(FacebookUser)
class FacebookUserAdmin(admin.ModelAdmin):
    pass


@admin.register(TwitterUser)
class TwitterUserAdmin(admin.ModelAdmin):
    pass


@admin.register(GitHubUser)
class GitHubUserAdmin(admin.ModelAdmin):
    pass


@admin.register(GitHubRelation)
class GitHubRelationAdmin(admin.ModelAdmin):
    pass
