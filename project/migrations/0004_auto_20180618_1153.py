# Generated by Django 2.0.4 on 2018-06-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20180521_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Tech',
                'verbose_name_plural': 'Techs',
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='tech',
        ),
        migrations.AddField(
            model_name='project',
            name='tech',
            field=models.ManyToManyField(to='project.Tech'),
        ),
    ]