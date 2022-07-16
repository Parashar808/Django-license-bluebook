from django.contrib import admin

from license.views import Fine

# Register your models here.
from .models import Nationalid, bluebook, license,License_Fine,Bluebook_Fine

admin.site.register(license)
admin.site.register(bluebook)
admin.site.register(Nationalid)
admin.site.register(License_Fine)
admin.site.register(Bluebook_Fine)


