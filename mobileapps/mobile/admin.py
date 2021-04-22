from django.contrib import admin

# Register your models here.
from mobile.models import Brands,Mobile,Orders
admin.site.register(Brands)
admin.site.register(Mobile)
admin.site.register(Orders)