from django.contrib import admin

from .models import (
    Product,
    Thumbnail,
    MyProducts,
    ProductRating,
    CuratedProducts,
)


class ThumbnailInline(admin.TabularInline):
    extra = 0
    model = Thumbnail


class ProductAdmin(admin.ModelAdmin):
    inlines = [ThumbnailInline]
    list_display = ["__str__", "description", "price", "sale_price"]
    search_fields = ["title", "description"]
    list_filter = ["price", "sale_price"]
    list_editable = ["sale_price"]

    class Meta:
        model = Product


admin.site.register(Thumbnail)

admin.site.register(Product, ProductAdmin)

admin.site.register(ProductRating)

admin.site.register(MyProducts)

admin.site.register(CuratedProducts)


