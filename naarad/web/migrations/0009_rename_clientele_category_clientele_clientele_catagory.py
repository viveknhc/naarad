# Generated by Django 5.1.4 on 2024-12-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_clientele'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientele',
            old_name='clientele_category',
            new_name='clientele_catagory',
        ),
    ]