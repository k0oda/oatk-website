from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    content = models.TextField() # TODO: WYSIWYG
    image = models.ImageField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title
