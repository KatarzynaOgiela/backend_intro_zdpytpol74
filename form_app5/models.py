from django.db import models


# Create your models here.
class Task(models.Model):
    name =models.CharField(max_length=64)

    def str(self):
        return f"Task {self.id},{self.name}"