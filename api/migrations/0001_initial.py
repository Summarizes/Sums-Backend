# Generated by Django 4.1.2 on 2023-02-11 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('bundle_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=16384, null=True)),
                ('price_thb', models.FloatField()),
                ('owner_id', models.ForeignKey(db_column='owner_id', on_delete=django.db.models.deletion.CASCADE, to='api.account')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.CharField(blank=True, max_length=16384, null=True)),
                ('url', models.CharField(max_length=1024)),
                ('is_preview', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=128)),
                ('name_th', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('payment_method_id', models.AutoField(primary_key=True, serialize=False)),
                ('citizen_id', models.CharField(max_length=128, unique=True)),
                ('bank', models.CharField(max_length=32)),
                ('qr_code', models.CharField(max_length=1000)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_thb', models.FloatField()),
                ('buyer_id', models.ForeignKey(db_column='buyer_id', on_delete=django.db.models.deletion.CASCADE, related_name='payment_buyer_id', to='api.account')),
                ('seller_id', models.ForeignKey(db_column='seller_id', on_delete=django.db.models.deletion.CASCADE, related_name='payment_seller_id', to='api.account')),
            ],
        ),
        migrations.CreateModel(
            name='BundlePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_thb', models.FloatField()),
                ('bundle_id', models.ForeignKey(db_column='bundle_id', on_delete=django.db.models.deletion.CASCADE, to='api.bundle')),
                ('payment_id', models.ForeignKey(db_column='payment_id', on_delete=django.db.models.deletion.CASCADE, to='api.payment')),
            ],
        ),
        migrations.AddField(
            model_name='bundle',
            name='subject_id',
            field=models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.CASCADE, to='api.subject'),
        ),
    ]
