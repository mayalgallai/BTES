# Generated by Django 4.2.16 on 2024-11-22 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_remove_payment_ticket_payment_payment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refundrequest',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('regular', 'Regular User'), ('publisher', 'Publisher'), ('admin', 'Admin')], default='regular', max_length=20),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]