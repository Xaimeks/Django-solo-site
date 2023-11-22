from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse




class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_title = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/')


    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title}, {self.author}'


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Comments(models.Model):
    text_comments = models.TextField('Текст комментария,', max_length=2000)
    email = models.EmailField()
    user_name = models.CharField('Имя пользователя', max_length=20)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE  )

    def __str__(self):
        return f'{self.text_comments}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



