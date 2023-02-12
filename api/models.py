from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=128)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    profile_picture = models.ImageField(upload_to='profile/',null=True,blank=True)

class PaymentMethod(models.Model):
    account_id = models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True,db_column='account_id')
    citizen_id = models.CharField(max_length=128,unique=True)
    bank = models.CharField(max_length=32)
    qr_code = models.ImageField(upload_to='payment_qr/')

class Subject(models.Model):
    subject_id = models.CharField(max_length=10,primary_key=True)
    name_en = models.CharField(max_length=128)
    name_th = models.CharField(max_length=128)

class Bundle(models.Model):
    bundle_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(Account,on_delete=models.CASCADE,db_column="owner_id")
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE,db_column="subject_id")
    description = models.CharField(max_length=16384,null=True,blank=True)
    price_thb = models.FloatField()

class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    bundle_id = models.ForeignKey(Bundle,on_delete=models.CASCADE,db_column='bundle_id')
    name = models.CharField(max_length=128,null=True,blank=True)
    description = models.CharField(max_length=16384,null=True,blank=True)
    url = models.CharField(max_length=1024)
    is_preview = models.BooleanField(default=False)

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    buyer_id = models.ForeignKey(Account,on_delete=models.CASCADE,db_column='buyer_id',related_name='payment_buyer_id')
    seller_id = models.ForeignKey(Account,on_delete=models.CASCADE,db_column='seller_id',related_name='payment_seller_id')
    total_thb = models.FloatField()

class BundlePayment(models.Model):
    payment_id = models.ForeignKey(Payment,on_delete=models.CASCADE,db_column='payment_id')
    bundle_id = models.ForeignKey(Bundle,on_delete=models.CASCADE,db_column='bundle_id')
    price_thb = models.FloatField()