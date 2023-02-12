from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import PaymentMethodSerializer
from rest_framework.parsers import MultiPartParser, FormParser


@api_view([GET,POST,PUT,DELETE])
@parser_classes([MultiPartParser,FormParser])
def manage_payment_method(request,account_id:int):
    account = Account.objects.get(account_id=account_id)

    if request.method == POST:
        request.data['account_id'] = account.account_id
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    else:
        try:
            paymeth = PaymentMethod.objects.get(account_id=account_id)
            
            if request.method == GET:
                serializer = PaymentMethodSerializer(paymeth)
                return Response(serializer.data,status=status.HTTP_200_OK)
            
            elif request.method == PUT:
                serializer = PaymentMethodSerializer(paymeth,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            elif request.method == DELETE:
                paymeth.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        except PaymentMethod.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        