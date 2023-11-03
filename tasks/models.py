from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

userforeing = get_user_model()



class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    datetime_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(userforeing, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-datetime_created"]
    
    
    def __str__(self) -> str:
        return f"{self.name} --------- {self.user} ---------- {self.completed} ----------- {self.datetime_created}"