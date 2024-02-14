# Generated by Django 5.0.2 on 2024-02-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_alter_certificate_expiration_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='expiration_month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10, null=True, verbose_name='Expiration Month'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='issue_month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10, null=True, verbose_name='Issue Month'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10, null=True, verbose_name='End Month'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10, null=True, verbose_name='Start Month'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10, null=True, verbose_name='End Month'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_month',
            field=models.CharField(blank=True, choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=10, null=True, verbose_name='Start Month'),
        ),
    ]
