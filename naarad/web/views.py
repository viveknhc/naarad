from django.shortcuts import render
from web.models import Service,Gallery,Film_Festival,Media_Image,Clientele,Contact,CSR,CSRAddOnContent,Testimonials,Contact
from django.shortcuts import render,get_object_or_404


def index(request):
    gallery = Gallery.objects.all().order_by('-id')[:2]
    client = Clientele.objects.all()
    services = Service.objects.all()
    media_item = Media_Image.objects.all().order_by('-id')[:6]
    categories = Media_Image.objects.values_list('media_category', flat=True).distinct() 
    testimonial = Testimonials.objects.all().order_by('-id')[:2]
    context = {"is_index": True,
               "gallery":gallery,
               "client":client,
               "services":services,
               "media_item": media_item,
               "categories": categories,
               "testimonial":testimonial
               }
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)

def services(request):
    services = Service.objects.all()
    context = {
                "is_services": True,
               "services":services
               }
    return render(request, "web/services.html", context)

def servicesDetail(request,id):
    service= get_object_or_404(Service,id=id)
    context = {"is_services": True,"service":service}
    return render(request, "web/services-detail.html", context)

def gallery(request):
    gallery = Gallery.objects.all()
    context = {
                "is_gallery": True,
               "gallery":gallery
               }
    return render(request, "web/gallery.html", context)

def galleryDetail(request,id):
    gallery= get_object_or_404(Gallery,id=id)
    context = {
                "is_gallery": True,
                "gallery":gallery
               }
    return render(request, "web/gallery-detail.html", context)

def filmFestival(request):
    films = Film_Festival.objects.all()
    context = {
                "is_film": True,
               "films":films
               }
    return render(request, "web/film-festival.html", context)

def filmFestivalDetail(request,id):
    films= get_object_or_404(Film_Festival,id=id)
    context = {
                "is_film": True,
                "films":films
               }
    return render(request, "web/film-festival-detail.html", context)



def mediaPage(request):
    media_item = Media_Image.objects.all()
    categories = Media_Image.objects.values_list('media_category', flat=True).distinct() 
    context = {
        "is_media_page": True,
        "media_item": media_item,
        "categories": categories
               }
    return render(request, "web/media.html", context)


def clientele(request):
    clientele_all = Clientele.objects.all()
    clientele_catagory = Clientele.objects.values_list('clientele_catagory', flat=True).distinct()
    context = {
        "is_clientele": True,
        "clientele_all": clientele_all,
        "clientele_catagory": clientele_catagory  # Fixed the extra space here
    }
    return render(request, "web/clientele.html", context)





def testimonial(request):
    testimonial = Testimonials.objects.all()
    context = {
        "is_testimonial": True,
        "testimonial": testimonial,
               }
    return render(request, "web/testimonials.html", context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_save = Contact(name = name,email = email,subject = subject,message = message)
        contact_save.save()
    
    context = {
        "is_contact": True,
               }
    return render(request, "web/contactus.html", context)

def csr(request):
    csr = CSR.objects.all()
    context = {
        "is_csr": True,
        "csr": csr,
               }
    return render(request, "web/csr.html", context)

def csrDetail(request,pk):
    csr_detail= get_object_or_404(CSR,pk=pk)
    context = {
        "is_csr": True,
        "csr_detail": csr_detail,
               }
    return render(request, "web/csr-detail.html", context)

