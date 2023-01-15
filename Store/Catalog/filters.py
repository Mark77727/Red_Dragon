import django_filters

""" import models """

from .models import Catalog

""" filters brand """


class CatalogFilter(django_filters.FilterSet):
    class Meta:
        model = Catalog
        fields = ['brand',
                  'GPU',
                  'memory_type',
                  'power_connector',
                  'video_connector',
                  'video_memory_capacity',
                  'frequency_GPU',
                  'video_card_length']

