from django.db import models

# Create your models here.
class article(models.Model):
    cid = models.CharField(max_length=50)
    textid = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
