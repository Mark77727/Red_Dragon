from django.contrib import admin

"""import library """

from import_export.admin import ImportExportModelAdmin

"""import models"""

from.models import Catalog
from.models import Category


""" show model"""


class CatalogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Catalog, CatalogAdmin)


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

