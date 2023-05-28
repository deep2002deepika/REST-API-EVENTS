from django.db import models

# Create your models here.
class app(models.Model):
    type=models.CharField(max_length=10)
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    tagline=models.TextField()
    schedule=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    files=models.ImageField()
    moderator=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    sub_category=models.CharField(max_length=20)
    rigor_rank=models.IntegerField()
    #attendees=models.ArrayField()  #not using postgresql so arrayfield won't work
    

