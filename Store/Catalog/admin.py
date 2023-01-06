from django.contrib import admin

"""import library """

from import_export.admin import ImportExportModelAdmin

"""import models"""

from.models import Catalog
from.models import Category
from.models import Brand
from.models import GPU
from.models import ManufacturerGPU
from.models import MemoryType
from.models import PowerConnector
from.models import VideoConnector


"""show model"""


class CatalogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Catalog, CatalogAdmin)


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Brand, BrandAdmin)


class GPUAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(GPU, GPUAdmin)


class ManufacturerGPUAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(ManufacturerGPU, ManufacturerGPUAdmin)


class MemoryTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(MemoryType, MemoryTypeAdmin)


class PowerConnectorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(PowerConnector, PowerConnectorAdmin)


class VideoConnectorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(VideoConnector, VideoConnectorAdmin)
