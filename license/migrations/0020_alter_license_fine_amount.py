# Generated by Django 4.0.6 on 2022-11-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0019_alter_license_fine_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license_fine',
            name='amount',
            field=models.CharField(default='0', max_length=10, null='True'),
        ),
    ]
