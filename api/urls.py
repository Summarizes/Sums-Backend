from django.urls import path
from .views import account,payment_method
urlpatterns = [
    path('accounts',account.create_account),
    path('accounts/<int:account_id>',account.manage_account),

    path('accounts/<int:account_id>/payment-method',payment_method.manage_payment_method),
]