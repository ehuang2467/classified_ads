# Generated by Django 4.1 on 2023-09-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classified_ads', '0006_change_date_posted_verbose'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='text',
            field=models.CharField(default='PLACEHOLDER', max_length=1000),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default='PLACEHOLDER', max_length=1000),
        ),
    ]
