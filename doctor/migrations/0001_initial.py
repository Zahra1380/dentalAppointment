# Generated by Django 4.2.5 on 2023-10-04 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('about', '0006_aboutmodel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='DentalExperts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('cost', models.FloatField()),
                ('image', models.ImageField(null=True, upload_to='services')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
                ('telegram', models.CharField(max_length=500)),
                ('linkedin', models.CharField(max_length=500)),
                ('img', models.ImageField(default='/doctors/team-1.jpg', upload_to='doctors')),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('day', models.ManyToManyField(related_name='day_work', to='about.day')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors_expert', to='doctor.dentalexperts')),
                ('service', models.ManyToManyField(related_name='doctors', to='doctor.service')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='certificate')),
                ('explanation', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='doctor.doctor')),
            ],
        ),
    ]
