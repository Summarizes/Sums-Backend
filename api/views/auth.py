from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import AccountSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from ..utils import encryption
from uuid import uuid4
from time import time
from django.forms.models import model_to_dict

TOKEN_LIFETIME = 60 # 6 * 30 * 60  # (Second)

@api_view([POST])
def login(request):
    try:
        account = Account.objects.get(username=request.data['username'])
        access = AccountToken.objects.get(account_id=account.account_id)
        account_ser = AccountSerializer(account)

        if encryption(request.data['password']) == account.password:

            access.token = uuid4().hex
            access.expire_timestamp = int(time() + TOKEN_LIFETIME)
            access.save()

            return Response({
                **account_ser.data,
                "token": model_to_dict(access)
            },status=status.HTTP_202_ACCEPTED)
        
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view([POST])
def logout(request):
    try:
        account = Account.objects.get(username=request.data['username'])
        access = AccountToken.objects.get(account_id=account.account_id)

        if request.data['token'] == access.token:
            access.token = None
            access.expire_timestamp = None
            access.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view([POST])
def verify(request):
    try:
        account = Account.objects.get(username=request.data['username'])
        access = AccountToken.objects.get(account_id=account.account_id)

        if request.data['token'] == access.token and time() <= access.expire_timestamp:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            access.token = None
            access.expire_timestamp = None
            access.save()
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)