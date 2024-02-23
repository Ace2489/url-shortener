from django.db import models

class Url(models.Model):
    longUrl = models.URLField(unique=True)
    shortUrl = models.URLField(unique=True)

    def __str__(self) -> str:
        return f'{self.longUrl} => {self.shortUrl}'