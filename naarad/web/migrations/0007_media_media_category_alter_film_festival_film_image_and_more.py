# Generated by Django 5.1.4 on 2024-12-30 13:57

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='media_category',
            field=models.CharField(choices=[('', '-- select --'), ('Clipping', 'Clipping'), ('Dockets', 'Dockets')], default=1, max_length=125),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='film_festival',
            name='film_image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='film'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_image',
            field=versatileimagefield.fields.VersatileImageField(upload_to='media'),
        ),
    ]
