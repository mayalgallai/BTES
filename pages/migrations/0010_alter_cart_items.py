# Generated by Django 5.1.2 on 2024-11-07 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_event_available_tickets_alter_event_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='pages.event'),
        ),
    ]
