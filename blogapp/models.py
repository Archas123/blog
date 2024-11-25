from django.db import models
class Blog(models.Model):
# Create your models here.
     
     title = models.CharField(max_length=250)
     description = models.CharField(max_length=500)
     authorname = models.CharField(max_length=100)
     date = models.CharField(max_length=50)

     class Meta:
          db_table="blog"
 