from django.contrib import admin
from .models import Category, Commodity

class CommodityInlineForm():
    pass

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'category');
    search_fields = ('name', )
    readonly_fields = ('img_tag','color_features', 'shape_features')
    fieldsets = [
        (None, {'fields': ['name', 'category']}),
        ('Picture', {'fields': ['img', 'img_tag']}),
        ('Color_Features', {'fields':['color_features'], 'classes': ['collapse']}),
        ('Shape_Features', {'fields':['shape_features']}),
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Commodity, CommodityAdmin)
