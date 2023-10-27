from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_registration = models.DateField()
    role = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.role}'


class Task(models.Model):
    task = models.CharField(max_length=255)
    date_of_creation = models.DateField()
    status = models.BooleanField()
    priority = models.CharField(max_length=255)
    executor = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task} - {self.executor} - {self.priority}\n{self.date_of_creation} - {self.status}'
