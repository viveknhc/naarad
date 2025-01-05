from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("services-detail/<str:id>", views.servicesDetail, name="services-detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery-detail/<str:id>", views.galleryDetail, name="gallery-detail"),
    path("film-festival/", views.filmFestival, name="film-festival"),
    path("film-festival-detail/<str:id>", views.filmFestivalDetail, name="film-festival-detail"),
    path("media-page/", views.mediaPage, name="media-page"),
    path("clientele/", views.clientele, name="clientele"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("contact/", views.contact, name="contact"),
    path("csr/", views.csr, name="csr"),
    path("csr-detail/<str:pk>", views.csrDetail, name="csr-detail"),
    
    
]