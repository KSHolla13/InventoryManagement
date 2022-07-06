from django.db import models
from users_app.models import CustomUser

# Create your models here.
class book(models.Model):
    manage = models.ForeignKey("users_app.CustomUser", on_delete=models.CASCADE, default=None)
    Book = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.Book