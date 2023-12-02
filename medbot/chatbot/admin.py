from django.contrib import admin
from .models import images
admin.site.register(images)
fields = ['image_tag']
readonly_fields = ['image_tag']
