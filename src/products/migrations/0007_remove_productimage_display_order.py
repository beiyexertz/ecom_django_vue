# Generated by Django 2.2.1 on 2019-11-20 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20191113_0459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='display_order',
        ),
    ]