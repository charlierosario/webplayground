from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    # list_display = ('title', 'order')
    readonly_fields = ('created', 'updated')
    exclude = ('order',)
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
