from django.db import models


class Story(models.Model):
    genre = models.CharField(max_length=100)
    main_character = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    mood = models.CharField(max_length=100)
    story_length = models.CharField(max_length=50)

    title = models.CharField(max_length=255)
    content = models.TextField()

    quote = models.TextField(blank=True)
    quote_author = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
