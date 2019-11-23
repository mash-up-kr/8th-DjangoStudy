from django.db import models
from django.utils import timezone


class HashTag(models.Model):
    name = models.CharField('태그명', max_length=30)

    def __str__(self):
        return self.name


class InstagramPost(models.Model):
    title = models.CharField('제목', max_length=30)
    # 가장 일반적인 Many-to-many (중개모델도 아니고 재귀적이지도 않음)
    tags = models.ManyToManyField(
        'HashTag', blank=True,
    )
    # 중개모델을 사용하는 Many-to-many
    like_users = models.ManyToManyField(
        'InstagramUser', through='InstagramPostLike', blank=True,
    )

    def __str__(self):
        return self.title


# 중개모델이며 재귀적이지 않은 관계
class InstagramUser(models.Model):
    name = models.CharField('이름', max_length=30)

    def __str__(self):
        return self.name


class InstagramPostLike(models.Model):
    """
    중개모델 (Intermediate model)
    """
    post = models.ForeignKey(InstagramPost, on_delete=models.CASCADE)
    user = models.ForeignKey(InstagramUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


# 중개모델이 아니면서 재귀적이며 대칭적인 관계
# Like 페이스북 친구, 내가 맺으면 너도 자동으로 맺어짐
class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self', blank=True,
    )

    def __str__(self):
        return self.name


# 중개모델이 아니면서 재귀적이며 비대칭 관계
class TwitterUser(models.Model):
    name = models.CharField(max_length=30)
    following = models.ManyToManyField(
        'self', symmetrical=False, blank=True,
    )

    def __str__(self):
        return self.name


# 중개모델이며 재귀적이며 비대칭관계
class GitHubUser(models.Model):
    name = models.CharField(max_length=30)
    following = models.ManyToManyField(
        'self', symmetrical=False, through='GitHubRelation', blank=True,
    )

    def __str__(self):
        return self.name


class GitHubRelation(models.Model):
    from_user = models.ForeignKey(
        GitHubUser, on_delete=models.CASCADE, related_name='relation_set_from_user',
    )
    to_user = models.ForeignKey(
        GitHubUser, on_delete=models.CASCADE, related_name='relation_set_to_user')
    created_at = models.DateTimeField(default=timezone.now)
