from django.shortcuts import render
from web.models import Service,Gallery
from django.shortcuts import render,get_object_or_404


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_index": True}
    return render(request, "web/about.html", context)

def services(request):
    services = Service.objects.all()
    context = {
                "is_index": True,
               "services":services
               }
    return render(request, "web/services.html", context)

def servicesDetail(request,id):
    service= get_object_or_404(Service,id=id)
    context = {"is_index": True,"service":service}
    return render(request, "web/services-detail.html", context)

def gallery(request):
    gallery = Gallery.objects.all()
    context = {
                "is_index": True,
               "gallery":gallery
               }
    return render(request, "web/gallery.html", context)

def galleryDetail(request):
    context = {
                "is_index": True,
               }
    return render(request, "web/gallery.html", context)

