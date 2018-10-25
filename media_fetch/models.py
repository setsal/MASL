from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class news(models.Model):
    mid = models.ForeignKey(
        company, on_delete=models.CASCADE
    )
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
