# Generated by Django 4.1 on 2023-09-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_ads', '0013_add_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
