from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    town = models.CharField(max_length=20)
    po = models.CharField(max_length=20)
    dist = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

