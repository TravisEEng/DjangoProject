from django.db import models

# Create your models here.
class Topic(models.Model):
    #A topic I am learning about
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        #return string representation of models
        return self.text

class Entry(models.Model):
    #Something specific learned about a topicself.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #Return a string representation of the modelself.
        if(len(self.text) > 50):
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
