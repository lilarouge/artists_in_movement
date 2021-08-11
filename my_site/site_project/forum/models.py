from django.db import models


class Discussion(models.Model):
    name= models.CharField(max_length=30)
    topic= models.CharField(max_length=300, null=True)
    text = models.CharField(max_length=1000)

 
    def __str__(self):
        return str(self.topic)

class Comment(models.Model):
    name= models.CharField(max_length=30)
    discussion= models.ForeignKey(Discussion,on_delete=models.CASCADE)
    content= models.CharField(max_length=2000)