from solo.admin import SingletonModelAdmin

from django.contrib import admin

from .models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)
