# Generated by Django 5.0.2 on 2024-02-14 11:48

from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0006_user_interests_alter_user_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.TextField(default='exit', verbose_name='Interests'),
            preserve_default=False,
        ),
    ]