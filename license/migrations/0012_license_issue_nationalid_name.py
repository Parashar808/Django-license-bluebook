# Generated by Django 4.0.4 on 2022-07-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0011_remove_nationalid_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='issue',
            field=models.CharField(default='not-issued', max_length=10),
        ),
        migrations.AddField(
            model_name='nationalid',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
