from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=200, default="--null--")
    project_id = models.CharField(max_length=20, primary_key=True)
    status = models.BooleanField()
    visits = models.IntegerField()
    team_presence = models.BooleanField()

    def __str__(self):
        return self.project_title