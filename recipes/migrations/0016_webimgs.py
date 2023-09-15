# Generated by Django 4.2.4 on 2023-09-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebImgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('thumbnail', models.ImageField(upload_to='web_imgs/')),
            ],
        ),
    ]