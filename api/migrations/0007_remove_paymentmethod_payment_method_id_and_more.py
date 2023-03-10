# Generated by Django 4.1.2 on 2023-02-12 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_paymentmethod_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='payment_method_id',
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='account_id',
            field=models.OneToOneField(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.account'),
        ),
    ]
