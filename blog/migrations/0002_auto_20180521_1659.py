# Generated by Django 2.0.4 on 2018-05-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='seo_desc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='seo_desc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
