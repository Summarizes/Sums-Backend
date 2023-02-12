from ..utils import encryption
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from django.forms.models import model_to_dict

@api_view([GET,POST,PUT,DELETE])
def manage_payment_method(request):
    if request.method == POST:
        paymed = PaymentMethod(
            
        )
        