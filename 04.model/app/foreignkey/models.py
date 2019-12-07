from django.db import models


class Post(models.Model):
    title = models.CharField('제목', max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('내용', blank=True)

    def __str__(self):
        return f'{self.post.title}글 의 댓글 {self.content}'


class DjangoStudyMember(models.Model):
    name = models.CharField('이름', max_length=20)
    leader = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
