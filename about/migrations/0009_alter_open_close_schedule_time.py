# Generated by Django 4.2.5 on 2023-10-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_open_close_close_open_close_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='open_close',
            name='schedule_time',
            field=models.ManyToManyField(null=True, related_name='open_close', to='about.scheduletime'),
        ),
    ]