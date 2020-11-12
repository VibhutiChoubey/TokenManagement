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

    # @property
    # def delete_unallocated_tokens_after_five_minutes(self):
    #     print('here')
    #     # Token.objects.filter(
    #     #     updated_at__lt=timezone.now()-timezone.timedelta(minutes=5)
    #     # ).delete()
    #     if self.user:
    #         time = self.updated_at + datetime.timedelta(minutes=1)
    #         if time < datetime.datetime.now():
    #             token = Token.objects.get(pk=self.pk)
    #             token.delete()
    #             return True
    #         else:
    #             return False
    #     else:
    #         time = self.updated_at + datetime.timedelta(minutes=5)
    #         if time < datetime.datetime.now():
    #             token = Token.objects.get(pk=self.pk)
    #             token.delete()
    #             return True
    #         else:
    #             return False
