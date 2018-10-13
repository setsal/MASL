from django.db import models

# Article Model
class article(models.Model):
    cid = models.CharField(max_length=50)
    textid = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)


# Club Model
class club(models.Model):
    cid = models.CharField(max_length=30)
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
