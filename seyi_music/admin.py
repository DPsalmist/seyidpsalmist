from django.contrib import admin
from .models import Track, ImageGallery, Video_Gallery, Graphics, Signature

# Register your models here.
admin.site.register(ImageGallery)
admin.site.register(Video_Gallery)
admin.site.register(Track)
admin.site.register(Graphics)
admin.site.register(Signature)