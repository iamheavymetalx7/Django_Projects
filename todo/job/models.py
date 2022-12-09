from django.db import models

# Create your models here.


from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title