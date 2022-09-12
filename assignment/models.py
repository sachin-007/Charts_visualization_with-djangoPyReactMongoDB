# from pyexpat import model
from django.db import models

# Create your models here.

class jsondatas(models.Model):
    assid=models.AutoField(primary_key=True)
    end_year=models.IntegerField()
    intensity=models.IntegerField()
    sector=models.CharField(max_length=200)
    topic=models.CharField(max_length=200)
    insight=models.CharField(max_length=200)
    url=models.CharField(max_length=255)
    region=models.CharField(max_length=255)
    start_year=models.IntegerField()
    impact=models.CharField(max_length=255)
    added=models.DateTimeField(auto_now_add=True, auto_now=False)
    published=models.DateTimeField(auto_now_add=True, auto_now=False)
    country=models.CharField(max_length=255)
    relevance=models.IntegerField()
    pestle=models.CharField(max_length=255)
    source=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    likelihood=models.IntegerField()
    # likethat=models.IntegerField()
