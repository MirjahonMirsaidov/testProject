from django.db import models


class Items(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    rank = models.IntegerField()
    quantity = models.IntegerField(null=True)
    verified = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Samples(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    item_id = models.CharField(max_length=255)
    date = models.DateField()
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name
