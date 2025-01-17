from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

MEDIA_CHOICE = (("", "-- select --"),("Clipping", "Clipping"),("Dockets", "Dockets"))
CLIENTELE_CHOICE = (("", "-- select --"),("ART CULTURE AND SPIRITUALISM", "ART CULTURE AND SPIRITUALISM"),("BOOK LAUNCHES", "BOOK LAUNCHES"),("CORPORATES", "CORPORATES"),("FILMS", "FILMS"),("PERSONALITIES", "PERSONALITIES"),("RESTAURANTS", "RESTAURANTS"),("TV SHOW", "TV SHOW"),("WELLNESS BEAUTY AND SPA", "TWELLNESS BEAUTY AND SPA")) 

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
    

class Film_Festival(models.Model):
    film_title = models.CharField(max_length=100)
    film_image = VersatileImageField(upload_to = "film")
    who_we_are = HTMLField()
    where_we_are = HTMLField()
    what_you_get = HTMLField()
    choose_your_competition = HTMLField()
    who_we_want = HTMLField()
    what_we_accept = HTMLField()
    terms_and_regulations = HTMLField()
    
    def __str__(self):
        return self.film_title
    

class Media_Image(models.Model):
    media_category = models.CharField(max_length=125,choices=MEDIA_CHOICE)
    media_title = models.CharField(max_length=100)
    media_image = VersatileImageField(upload_to = "media")
    
    def __str__(self):
        return self.media_title



class Clientele(models.Model):
    clientele_catagory = models.CharField(max_length=125,choices=CLIENTELE_CHOICE)
    clientele_title = models.CharField(max_length=100)
    clientele_image = VersatileImageField(upload_to = "media")
    
    def __str__(self):
        return self.clientele_title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class CSR(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='csr_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class CSRAddOnContent(models.Model):
    csr = models.ForeignKey(CSR, related_name='add_on_contents', on_delete=models.CASCADE)
    sub_heading = models.CharField(max_length=200)
    paragraph = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='csr_addon_images/', blank=True, null=True)

    def __str__(self):
        return self.sub_heading
    

class Testimonials(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url