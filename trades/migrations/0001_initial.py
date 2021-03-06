# Generated by Django 2.1.2 on 2018-10-17 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(choices=[('BIN', 'BINS'), ('BAG', 'BAGS'), ('CARTON', 'CARTONS'), ('BBAG', 'BIG BAGS'), ('PBAG', 'POLY BAGS'), ('SSACK', 'SUPER SACKS'), ('TIN', 'TINS'), ('PLBAG', 'PLASTIC BAGS'), ('BOX', 'BOXES')], default='BAG', max_length=10, verbose_name='package')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='weight')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='price')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='is accepted')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('CMR', 'CMR'), ('QC', 'QUALITY CERTIFICATE'), ('ED', 'EXPORT DECLARATION')], max_length=50, verbose_name='Document name')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='quantity')),
                ('details', models.TextField(verbose_name='details')),
                ('prod_date', models.DateField(blank=True, null=True, verbose_name='production date')),
                ('exp_date', models.DateField(blank=True, null=True, verbose_name='expiry date')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='price')),
                ('metric', models.CharField(choices=[('KG', 'Kilogram'), ('MT', 'Metric Tonnes'), ('LBS', 'Pounds')], default='KG', max_length=5, verbose_name='metric')),
                ('is_closed', models.BooleanField(default=False, verbose_name='is closed')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='trades.Crop')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='trades.Product'),
        ),
        migrations.AddField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='trades.Product'),
        ),
    ]
