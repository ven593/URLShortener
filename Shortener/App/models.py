from django.db import models


# Create your models here.
class URLShortener(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"