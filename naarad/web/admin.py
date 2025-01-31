from django.contrib import admin
from web.models import Service,Gallery,Film_Festival,Media_Image,Clientele,Contact,CSRAddOnContent,CSR,Testimonials
from django.utils.html import format_html




class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_gif_image_preview','service_title', 'service_description')

    def service_gif_image_preview(self, obj):
        if obj.service_gif_image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.service_gif_image.url)
        return "No Image"
    service_gif_image_preview.short_description = "Service GIF Preview"
admin.site.register(Service, ServiceAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('gallery_image_preview', 'gallery_title', 'gallery_date', 'gallery_description')

    def gallery_image_preview(self, obj):
        if obj.gallery_image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.gallery_image.url)
        return "No Image"
    gallery_image_preview.short_description = "Image Preview"

admin.site.register(Gallery, GalleryAdmin)

# admin.site.register(Gallery)
admin.site.register(Film_Festival)
admin.site.register(Media_Image)
admin.site.register(Clientele)
admin.site.register(Contact)
admin.site.register(Testimonials)


class CSRAddOnContentInline(admin.StackedInline):
    model = CSRAddOnContent
    extra = 1  # Number of empty fields to display initially
    fields = ('sub_heading', 'paragraph', 'image')  # Specify the fields to display

@admin.register(CSR)
class CSRAdmin(admin.ModelAdmin):
    inlines = [CSRAddOnContentInline]
    list_display = ('title',)