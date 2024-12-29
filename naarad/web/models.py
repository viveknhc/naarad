from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_description = HTMLField()
    service_gif_image = VersatileImageField(upload_to = "service")
    service_main_image = VersatileImageField(upload_to = "service")
    
    def __str__(self):
        return self.service_title
    
class Gallery(models.Model):
    gallery_title = models.CharField(max_length=100)
    gallery_date = models.DateTimeField(null=True, blank=True)
    gallery_description = HTMLField()
    gallery_image = VersatileImageField(upload_to = "gallery")
    
    def __str__(self):
        return self.gallery_title