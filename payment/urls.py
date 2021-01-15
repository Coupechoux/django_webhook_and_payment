from django.urls import path
from . import views

urlpatterns = [
	path('', views.payment_button_view, name='payment_button'),
	path('test-json', views.json_test), 
	path('checkout/', views.get_checkout_session, name="checkout"),
	path('checkout/success/', views.success_view, name='success'),
	path('checkout/cancel/', views.cancel_view, name='cancel'),
	path('checkout/webhook/', views.webhook_confirm_payment),
]