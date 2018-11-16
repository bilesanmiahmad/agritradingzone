# Generated by Django 2.1.2 on 2018-11-15 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0005_auto_20181030_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=30, verbose_name='Crop to sell')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Quantity')),
                ('metric', models.CharField(choices=[('KG', 'Kilogram'), ('MT', 'Metric Tonnes'), ('LBS', 'Pounds')], max_length=10, verbose_name='Metric')),
                ('details', models.TextField(blank=True, verbose_name='Details')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price per metric')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='metric',
            field=models.CharField(choices=[('KG', 'Kilogram'), ('MT', 'Metric Tonnes'), ('LBS', 'Pounds')], default='KG', max_length=10, verbose_name='metric'),
        ),
    ]
