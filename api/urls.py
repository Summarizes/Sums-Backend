from django.urls import path
from .views import account,auth,payment_method
urlpatterns = [
    path('accounts',account.create_account),
    path('accounts/<int:account_id>',account.manage_account),

    path('auth/login',auth.login),
    path('auth/logout',auth.logout),
    path('auth/verify',auth.verify),

    path('accounts/<int:account_id>/payment-method',payment_method.manage_payment_method),
]