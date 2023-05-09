from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь создавший пост', null=True, blank=True)
    title=models.CharField(verbose_name='Заголовок', max_length=255, default='', null=True, blank=True)
    text=models.TextField(verbose_name='Описание')
    date_post=models.DateTimeField(default=timezone.now, verbose_name='Дата создания поста')

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Посты'

    def __str__(self) -> str:
        return self.title
    
class AboutUs(models.Model):
    whatsapp_link = models.URLField(max_length=200, verbose_name='Ссылка на WhatsApp', null=True, blank=True)
    telegram_link = models.URLField(max_length=200, verbose_name='Ссылка на Telegram', null=True, blank=True)
    text = models.TextField(verbose_name='Текст о нас', null=True, blank=True)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'




# Create your models here.
