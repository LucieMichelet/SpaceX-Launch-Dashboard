from django.db import models

# Create your models here.
class Launch(models.Model):
    mission_name = models.CharField(max_length = 100)
    launch_date = models.DateTimeField()
    rocket_name = models.CharField(max_length = 100)
    details = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.mission_name