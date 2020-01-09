from django.db import models

# Create your models here.
class Topic(models.Model):
    #A topic I am learning about
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        #return string representation of models
        return self.text
