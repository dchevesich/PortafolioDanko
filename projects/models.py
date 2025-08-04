from django.db import models
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web_app', 'Aplicación Web'),
        ('api', 'API REST'),
        ('automation', 'Automatización'),
        ('iot', 'IoT'),
        ('other', 'Otro'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=150, help_text="Descripción corta para preview", blank=True)
    image = models.CharField(max_length=255, blank=True, null=True, help_text="Path to static image (e.g., 'img/calculadora.PNG')")
    github_link = models.URLField(max_length=200, blank=True, null=True)
    demo_link = models.URLField(max_length=200, blank=True, null=True)
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies (e.g., Python, Django, PostgreSQL)")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web_app')
    featured = models.BooleanField(default=False, help_text="Marcar como proyecto destacado")
    achievements = models.TextField(blank=True, help_text="Logros específicos del proyecto (separados por líneas)")
    created_date = models.DateField(default=timezone.now)
    order = models.IntegerField(default=0, help_text="Orden de visualización (menor número = primero)")

    class Meta:
        ordering = ['-featured', 'order', '-created_date']

    def __str__(self):
        return self.name
    
    @property
    def technologies_list(self):
        """Retorna las tecnologías como una lista"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []
    
    @property
    def achievements_list(self):
        """Retorna los logros como una lista"""
        if self.achievements:
            return [achievement.strip() for achievement in self.achievements.split('\n') if achievement.strip()]
        return []