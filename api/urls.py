from django.urls import path
from .views import account
urlpatterns = [
    path('accounts',account.create_account),
    path('accounts/<int:account_id>',account.manage_account),
]