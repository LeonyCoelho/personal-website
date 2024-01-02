from django.db import models

class ProjectImage(models.Model):
    project_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name

class Project(models.Model):
    project_title = models.CharField(max_length=200, null=True)
    project_tags = models.CharField(max_length=100, blank=True, null=True)
    project_images = models.ManyToManyField(ProjectImage)
    project_description = models.CharField(max_length=200, null=True)

