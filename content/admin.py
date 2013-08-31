from django.contrib import admin
from content.models import Page, Media
from adminsortable.admin import SortableAdmin, SortableStackedInline

class MediaInline(admin.StackedInline):
    model = Media
    extra = 1

class PageAdmin(SortableAdmin):
    inlines = [MediaInline]

admin.site.register(Page, PageAdmin)
