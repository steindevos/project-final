# Generated by Django 2.0.6 on 2018-08-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20180821_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='milk_type',
            field=models.CharField(choices=[['cow', 'Cow'], ['goat', 'Goat'], ['sheep', 'Sheep']], default='Cow', max_length=12),
        ),
    ]
