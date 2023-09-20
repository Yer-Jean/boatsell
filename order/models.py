from django.db import models


class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='лодка')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    # Когда сущности создаются пользователями желательно хранить время, когда оно создалось
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')

    def __str__(self):
        return f'{self.boat} от {self.email}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
