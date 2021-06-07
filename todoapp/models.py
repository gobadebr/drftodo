from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  completed = models.BooleanField(default=False, blank=True, null=True)
  startdate = models.DateField(blank=True,editable=True)
  enddate = models.DateField(blank=True,editable=True)
      
  def __str__(self):
    return self.title