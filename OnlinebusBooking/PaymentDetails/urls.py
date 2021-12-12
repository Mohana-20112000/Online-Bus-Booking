from django.urls import path
from . import views

urlpatterns = [
    path('payment-details/',views.PaymentList,name='payment-details'),
    path('payment-details/<int:pk>/',views.PaymentDetail,name='payment-detail'),
    path('add-payment/',views.addPayment,name='add-payment'),
    path('delete-payment/<int:pk>/',views.deletePayment,name='delete-payment'),

]