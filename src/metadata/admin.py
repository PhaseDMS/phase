from django.contrib import admin

from metadata.models import ValuesList, ListEntry
from metadata.handlers import populate_values_list_cache


class EntryInline(admin.TabularInline):
    model = ListEntry
    extra = 10


class ValuesListAdmin(admin.ModelAdmin):
    list_display = (
        "index",
        "name",
    )
    inlines = [EntryInline]

    def save_formset(self, request, form, formset, change):
        super(ValuesListAdmin, self).save_formset(request, form, formset, change)
        populate_values_list_cache()


admin.site.register(ValuesList, ValuesListAdmin)
