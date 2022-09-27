from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.last_name}-{self.first_name}'
