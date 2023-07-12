from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

    class Meta:
        db_table = 'project_management'

    def __str__(self):
        return self.name
