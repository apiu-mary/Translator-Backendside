from django.db import models

# Create your models here.
class Translation(models.Model):
    text_to_translate = models.TextField()
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_to_translate

