from django.contrib import admin
from .models import Image,Location,Category

# class LocationAdmin(admin.ModelAdmin):
#   filter_horizontal=('location')

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
