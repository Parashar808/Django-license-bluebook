# Generated by Django 4.0.6 on 2022-08-12 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0016_rename_name_license_fine_nid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license_fine',
            old_name='nid',
            new_name='national_id',
        ),
    ]
