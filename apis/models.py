from django.db import models

# Create your models here.
class Client(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.email


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    status = models.CharField(max_length=20, default="AVAILABLE")
    user = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
