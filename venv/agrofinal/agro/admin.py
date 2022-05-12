from django.contrib import admin
from .models import farmer
from .models import manager
from .models import product
from .models import inventory
from .models import stocks
# Register your models here.

admin.site.register(farmer)
admin.site.register(manager)
admin.site.register(product)
admin.site.register(inventory)
admin.site.register(stocks)
# admin.site.register()

