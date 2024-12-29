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
    
]