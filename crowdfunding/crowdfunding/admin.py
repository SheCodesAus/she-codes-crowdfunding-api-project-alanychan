from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.Projects)

#register link
admin.site.site_url = "/projects"
