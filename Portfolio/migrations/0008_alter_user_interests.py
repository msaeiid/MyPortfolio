# Generated by Django 5.0.2 on 2024-02-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0007_alter_user_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.TextField(null=True, verbose_name='Interests'),
        ),
    ]
