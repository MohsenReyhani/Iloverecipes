# Generated by Django 4.2.4 on 2023-08-18 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_profile_image_profile_fav_page_image_paths_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]