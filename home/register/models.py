from django.db import models


class register_user(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile = models.IntegerField()
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username


class register_pg(models.Model):
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    price = models.IntegerField()
    no_of_pg = models.IntegerField()
    def __str__(self):
        return self.company
