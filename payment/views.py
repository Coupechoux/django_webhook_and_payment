from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import stripe
from quick_site.settings import STRIPE_SECRET_API_KEY, STRIPE_PUBLIC_API_KEY


# Create your views here.
def payment_button_view(request):
	# return HttpResponse('Hello')
	data = {
		'STRIPE_PUBLIC_KEY': STRIPE_PUBLIC_API_KEY
	}
	return render(request, 'payment/button.html', data)
	
def json_test(request):
	data = {'a':4, 'b':'maison', 6: None}
	return JsonResponse(data)
	
def success_view(request):
	return HttpResponse('Payée')
	
def cancel_view(request):
	return HttpResponse('Annulée')
	
def get_checkout_session(request):
	stripe.api_key = STRIPE_SECRET_API_KEY
	checkout_session = stripe.checkout.Session.create(
		success_url=request.build_absolute_uri(reverse('success')),
		cancel_url=request.build_absolute_uri(reverse('cancel')),
		payment_method_types=["card"],
		line_items=[
			{
				'price':'price_1I8aCMAyG7d5yMdebfwoa98u',
				'quantity':1
			}
		], 
		mode="payment"
	)
	data = {
		"session_id":checkout_session['id'],
	}
	
	return JsonResponse(data)
	
@csrf_exempt
def webhook_confirm_payment(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY
	endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
	
	payload = request.body
	sig_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None

	try:
		event = stripe.Webhook.construct_event(
			payload, sig_header, endpoint_secret
		)
	except ValueError as e:
		# Invalid payload
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		# Invalid signature
		return HttpResponse(status=400)

	# Handle the event
	if event.type == 'payment_intent.succeeded':
		payment_intent = event.data.object # contains a stripe.PaymentIntent
		print('PaymentIntent was successful!')
		print(payment_intent)
	else:
		print('Unhandled event type {}'.format(event.type))
		
	return HttpResponse(status=200)