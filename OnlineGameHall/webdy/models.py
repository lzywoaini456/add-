from django.db import models
from user.models import User
# Create your models here.


class VideoType(models.Model):
    type_name = models.CharField(max_length=10, verbose_name='类型名称')
    type_introduction = models.CharField(max_length=30, verbose_name='类型介绍')

    def __str__(self):
        return self.type_name


class Video(models.Model):
    video_name = models.CharField(max_length=20, verbose_name='视频介绍')
    video_likes = models.IntegerField(verbose_name='点赞数')
    video_comment = models.IntegerField(verbose_name='评论数')
    video_files = models.CharField(max_length=40, verbose_name='文件路径')
    video_type = models.ForeignKey(to=VideoType, on_delete=models.CASCADE)
    video_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    video_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.video_name


class Likes(models.Model):
    l_video = models.IntegerField(verbose_name='视频id')
    l_user = models.IntegerField(verbose_name='用户id')
    l_type = models.IntegerField(default=0, verbose_name='视频类型id')


class VideoComment(models.Model):
    com_text = models.CharField(max_length=30, verbose_name='评论')
    com_ba = models.IntegerField(verbose_name='父亲评论id')
    com_video = models.IntegerField(verbose_name='视频id')
    com_user = models.IntegerField(verbose_name='用户id')

