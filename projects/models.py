from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    demo_link = models.URLField(max_length=200, blank=True, null=True)
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies (e.g., Python, Django, PostgreSQL)")

    def __str__(self):
        return self.name