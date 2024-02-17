# Generated by Django 5.0.2 on 2024-02-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='Credential_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Credential Id'),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Degree'),
        ),
        migrations.AlterField(
            model_name='education',
            name='field_of_study',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Field of Study'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Company Name'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='industry',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Industry'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='background/'),
        ),
    ]
