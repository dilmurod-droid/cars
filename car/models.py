from django.db import models

from users.models import CustomUser


class Car(models.Model):
    name=models.CharField(max_length=100)
    price = models.CharField(max_length=100000000000)
    brand=models.CharField(max_length=250,default="Chevrolet")
    description=models.TextField()
    photo = models.ImageField(upload_to='cars/img/', null=True, blank=True)
    available=models.BooleanField(db_default=True)
    def __str__(self):
        return f'{self.name}'

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.car.name}'