from django.db import models

# Create your models here.

class GameFor(models.Model):


    name = models.CharField(max_length=255, verbose_name='归属板块')

    def __str__(self):
        return self.name

class GameKind(models.Model):

    name = models.CharField(max_length=255, verbose_name='游戏名字', unique=True)
    type = models.CharField(max_length=255, verbose_name='游戏性质')
    time = models.DateField(verbose_name='发表日期')
    img = models.ImageField(upload_to='game_img', null=True, default=None, blank=True)

    kind = models.ManyToManyField(GameFor)

    def __str__(self):
        return self.name


