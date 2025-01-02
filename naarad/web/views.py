from django.shortcuts import render
from web.models import Service,Gallery,Film_Festival,Media,Clientele,Contact,CSR,CSRAddOnContent,Testimonials
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

def galleryDetail(request,id):
    gallery= get_object_or_404(Gallery,id=id)
    context = {
                "is_index": True,
                "gallery":gallery
               }
    return render(request, "web/gallery-detail.html", context)

def filmFestival(request):
    films = Film_Festival.objects.all()
    context = {
                "is_index": True,
               "films":films
               }
    return render(request, "web/film-festival.html", context)

def filmFestivalDetail(request,id):
    films= get_object_or_404(Film_Festival,id=id)
    context = {
                "is_index": True,
                "films":films
               }
    return render(request, "web/film-festival-detail.html", context)



def media(request):
    media_item = Media.objects.all()
    categories = Media.objects.values_list('media_category', flat=True).distinct() 
    context = {
        "is_index": True,
        "media_item": media_item,
        "categories": categories
               }
    return render(request, "web/media.html", context)


def clientele(request):
    clientele_all = Clientele.objects.all()
    clientele_catagory = Clientele.objects.values_list('clientele_catagory', flat=True).distinct()
    context = {
                "is_index": True,
               "clientele_all":clientele_all,
               "clientele_catagory ":clientele_catagory
               }
    return render(request, "web/clientele.html", context)


def media(request):
    media_item = Media.objects.all()
    categories = Media.objects.values_list('media_category', flat=True).distinct() 
    context = {
        "is_index": True,
        "media_item": media_item,
        "categories": categories
               }
    return render(request, "web/media.html", context)

def testimonial(request):
    testimonial = Testimonials.objects.all()
    context = {
        "is_index": True,
        "testimonial": testimonial,
               }
    return render(request, "web/testimonials.html", context)

def contact(request):
    
    context = {
        "is_index": True,
        "contact": contact,
               }
    return render(request, "web/contactus.html", context)

def csr(request):
    csr = CSR.objects.all()
    context = {
        "is_index": True,
        "csr": csr,
               }
    return render(request, "web/csr.html", context)

def csrDetail(request,pk):
    csr_detail= get_object_or_404(CSR,pk=pk)
    context = {
        "is_index": True,
        "csr_detail": csr_detail,
               }
    return render(request, "web/csr-detail.html", context)

