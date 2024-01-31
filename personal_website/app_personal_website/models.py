from django.db import models

class ProjectImage(models.Model):
    project_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name
    
class Tags(models.Model):
    tag_name = models.CharField(max_length=100)

class Project(models.Model):
    project_title = models.CharField(max_length=200, null=True)
    project_tags = models.ManyToManyField(Tags)
    project_images = models.ManyToManyField(ProjectImage)
    project_description = models.CharField(max_length=200, null=True)
    at_home = models.BooleanField(default=False)
    order = models.IntegerField(null=True)



