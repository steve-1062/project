# Generated by Django 4.0.4 on 2022-05-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('farmer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('farmer_name', models.CharField(max_length=30)),
                ('adhaar_n0', models.PositiveBigIntegerField()),
                ('phone_no', models.PositiveBigIntegerField()),
                ('photo', models.ImageField(upload_to='agro\\pics')),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('inventory_id', models.IntegerField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_no', models.PositiveBigIntegerField()),
                ('department', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=30)),
                ('product_img', models.ImageField(upload_to='agro\\pics')),
                ('quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('farmer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.farmer')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.manager')),
            ],
        ),
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('stock_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock_name', models.CharField(max_length=20)),
                ('available_quantity', models.FloatField()),
                ('price', models.FloatField()),
                ('inventory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.inventory')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.product')),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agro.manager'),
        ),
    ]
