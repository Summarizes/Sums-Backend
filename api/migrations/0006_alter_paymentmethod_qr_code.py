# Generated by Django 4.1.2 on 2023-02-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_account_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='qr_code',
            field=models.ImageField(upload_to='payment_qr/'),
        ),
    ]
