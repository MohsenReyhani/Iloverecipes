# Generated by Django 4.2.4 on 2023-08-17 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_usersaves_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersaves',
            name='imgpath',
        ),
    ]
