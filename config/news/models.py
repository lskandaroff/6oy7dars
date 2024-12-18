from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='post/photos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name