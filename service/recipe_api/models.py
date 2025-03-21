from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField()
    ingredients = models.JSONField(blank=True, default=list, null=True)
    instructions = models.JSONField(blank=True, default=list, null=True)
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | Rate: {self.rate} | CreatedAt: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
