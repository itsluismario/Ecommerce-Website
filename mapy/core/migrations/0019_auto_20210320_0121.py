# Generated by Django 3.1.7 on 2021-03-20 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210320_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='shipping_address',
            new_name='street_address',
        ),
    ]
