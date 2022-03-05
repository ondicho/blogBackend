from django.db import models

# Create your models here.

class Post(models.Model):
    category_choices=[('Motivation','Motivation'),('Art','Art'),('Technology','Technology'),('Finance','Finance')]
    title=models.TextField(max_length=32)
    category=models.CharField(choices=category_choices,max_length=32)
    description=models.TextField()

    def __str__(self):
        return str(self.title)
