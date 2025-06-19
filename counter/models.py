from django.db import models
from django.contrib.auth.models import User

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


