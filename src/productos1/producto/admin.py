from django.contrib import admin

# Register your models here.

from .models import Producto


class AdminProducto(admin.ModelAdmin):
    list_display = ["nombre","idT","fechaV"]
    list_filter = ["fechaV"]
    search_fields = ["nombre","idT"]
    class Meta:
        model = Producto

admin.site.register(Producto, AdminProducto)