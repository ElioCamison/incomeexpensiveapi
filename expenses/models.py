from django.db import models

from authentication.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user")
    name = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="owner")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="categories")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.amount} {self.date}"
