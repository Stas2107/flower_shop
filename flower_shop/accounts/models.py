from django.db import models

# Create your models here.
from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()  # Здесь вы можете использовать URL изображения (например, от внешнего хоста)

    def __str__(self):
        return self.name