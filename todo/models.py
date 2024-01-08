from django.db import models


class TodoModel(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование задачи")
    completed = models.BooleanField(verbose_name="Выполнена", default=False)

    def __str__(self):
        return self.name




# Create your models here.
