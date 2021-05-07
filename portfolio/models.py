from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    # video = models.FileField(upload_to='portfolio/videos/')
    # class Meta:
    #     verbose_name = 'video'
    #     verbose_name_plural = 'videos'

    def __str__(self):
        return self.title