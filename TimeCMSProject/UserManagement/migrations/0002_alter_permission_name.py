# Generated by Django 4.1.2 on 2022-10-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(default=None, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
