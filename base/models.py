from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  name = models.CharField(max_length = 200)
  balance = models.FloatField(default = 0)

class Transaction(models.Model):
  class Meta:
    ordering = ["datetime"]

  TRANSACTION_TYPE = {
    "dep": "Deposit",
    "wit": "Withdraw"
  }

  transaction_type = models.TextField(choices=TRANSACTION_TYPE)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  datetime = models.DateTimeField(auto_now_add=True)
  value = models.FloatField(null=True)

  def to_dict(self):
    return {
      'transaction_type': self.TRANSACTION_TYPE[self.transaction_type],
      'datetime': self.datetime.isoformat(),
      'value': self.value
    }