from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import AccountSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from ..utils import encryption

@api_view([POST])
def login(request):
    pass
