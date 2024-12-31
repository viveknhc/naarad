# Generated by Django 5.1.4 on 2024-12-30 13:45

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_film_festival'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_title', models.CharField(max_length=100)),
                ('media_image', versatileimagefield.fields.VersatileImageField(upload_to='gallery')),
            ],
        ),
    ]