# Generated by Django 4.0.6 on 2022-11-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0017_rename_nid_license_fine_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license_fine',
            name='amount',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
