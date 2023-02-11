from ..utils import encryption
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from django.forms.models import model_to_dict

@api_view([POST])
def create_account(request):
    account = Account(**{
        **request.data,
        "password": encryption(request.data['password'])
    })
    account.save()
    return Response(model_to_dict(account),status=status.HTTP_201_CREATED)

@api_view([GET,PUT,DELETE])
def manage_account(request,account_id:int):
    account = Account.objects.get(account_id=account_id)
    if request.method == GET:
        return Response(model_to_dict(account),status=status.HTTP_200_OK)
    elif request.method == PUT:
        account.firstname = request.data.get('firstname',account.firstname)
        account.lastname = request.data.get('lastname',account.lastname)
        account.save()
        return Response(model_to_dict(account),status=status.HTTP_202_ACCEPTED)
    elif request.method == DELETE:
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)