from django.contrib import admin

# Register your models here.

from .models import Translation

class TranslationAdmin(admin.ModelAdmin):
    list_display = ('text_to_translate', 'translated_text', 'created_at')
    # list_filter = ('created_at',)
    # search_fields = ('text_to_translate', 'translated_text')

admin.site.register(Translation, TranslationAdmin)

