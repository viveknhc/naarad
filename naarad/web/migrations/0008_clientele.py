# Generated by Django 5.1.4 on 2024-12-30 14:55

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_media_media_category_alter_film_festival_film_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientele',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientele_category', models.CharField(choices=[('', '-- select --'), ('ART CULTURE AND SPIRITUALISM', 'ART CULTURE AND SPIRITUALISM'), ('BOOK LAUNCHES', 'BOOK LAUNCHES'), ('CORPORATES', 'CORPORATES'), ('FILMS', 'FILMS'), ('PERSONALITIES', 'PERSONALITIES'), ('RESTAURANTS', 'RESTAURANTS'), ('TV SHOW', 'TV SHOW'), ('WELLNESS BEAUTY AND SPA', 'TWELLNESS BEAUTY AND SPA')], max_length=125)),
                ('clientele_title', models.CharField(max_length=100)),
                ('clientele_image', versatileimagefield.fields.VersatileImageField(upload_to='media')),
            ],
        ),
    ]
