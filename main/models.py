from django.db import models

#This class create a model to each project added using the admin page. 

class Project(models.Model):
    title = models.CharField(max_length=200)
    # Project title shown on the portfolio card.
    description = models.TextField()
    # Project image uploaded through the Django admin panel.
    image = models.ImageField(upload_to='projects/')
    # Optional GitHub repository link.
    github_link = models.URLField(blank=True)

# Returns the project title in the Django admin panel.
    def __str__(self):
        return self.title