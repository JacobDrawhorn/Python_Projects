from django.db import models
# create classes app
class djangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField()
    Instructor = models.CharField(max_length=50)
    Duration = models.FloatField()

