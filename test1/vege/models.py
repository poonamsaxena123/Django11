from django.db import models
from django.contrib.auth.models import User

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    # rating111 = models.IntegerField(default=0, null=True, blank=True,db_column="rating11")  


# db_column="new_rating"