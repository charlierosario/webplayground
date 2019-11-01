from django.contrib import admin
from .models import Persona, Codigo


class PageAdmin(admin.ModelAdmin):
    # list_display = ('title', 'order')
    readonly_fields = ('codigocurso','created','updated')
    ordering = ("-dni",)
    search_fields = ('dni',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)}


class CodigoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Codigo, CodigoAdmin)
admin.site.register(Persona, PageAdmin)
# Register your models here.
