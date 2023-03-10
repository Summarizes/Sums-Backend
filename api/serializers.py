from rest_framework import serializers
from .models import *
from .utils import encryption
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def create(self,validate_data):
        validate_data['password'] = encryption(validate_data['password'])
        return Account.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.firstname = validate_data.get('firstname',instance.firstname)
        instance.lastname = validate_data.get('lastname',instance.lastname)
        instance.profile_picture = validate_data.get('profile_picture',instance.profile_picture)
        instance.save()
        return instance

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"
    
    def create(self,validate_data):
        return PaymentMethod.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        instance.bank = validate_data.get("bank",instance.bank)
        instance.qr_code = validate_data.get("qr_code",instance.qr_code)
        instance.save()
        return instance
        