# Generated by Django 4.1.4 on 2023-01-11 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_remove_catalog_slug_alter_catalog_gpu_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
