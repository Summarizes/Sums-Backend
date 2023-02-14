from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import AccountSerializer
from rest_framework.parsers import MultiPartParser, FormParser

@api_view([POST])
@parser_classes([FormParser, MultiPartParser])
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        account_instance = serializer.save()
        access = AccountToken(account_id=account_instance)
        access.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

@api_view([GET,PUT,DELETE])
@parser_classes([FormParser, MultiPartParser])
def manage_account(request,account_id:int):
    try:
        account = Account.objects.get(account_id=account_id)

        if request.method == GET:
            serializer = AccountSerializer(account)
            return Response(serializer.data,status=status.HTTP_200_OK)

        elif request.method == PUT:
            serializer = AccountSerializer(account,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == DELETE:
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)