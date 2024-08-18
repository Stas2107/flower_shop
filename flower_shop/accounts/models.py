from django.db import models
from django.contrib.auth.models import User

# Модель для хранения информации о цветах
class Flower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()  # URL изображения

    def __str__(self):  # Исправлено на __str__
        return self.name

# Модель для хранения заказов
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flowers = models.ManyToManyField(Flower)  # Изменено на Flower
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Исправлено на __str__
        return f'Order {self.id} by {self.user.username}'