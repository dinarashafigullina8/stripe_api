from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
from stripe_api.models import Item
import stripe
from core import settings
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)




class ItemView(ListView):
    model = Item
    template_name = 'stripe_api/templates/stripe_api/item_list.html'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = Item.objects.filter(id=self.kwargs['id']).values('id','name', 'description', 'price').first()
        return context



class SuccessView(TemplateView):
    template_name = '/home/dinara/stripe_api/stripe_api/templates/stripe_api/success.html'


class CancelledView(TemplateView):
    template_name = '/home/dinara/stripe_api/stripe_api/templates/stripe_api/cancel.html'

@csrf_exempt
def create_checkout_session(request,id):
    item = Item.objects.filter(id=id)
    price_id = item.values('price_id')[0]['price_id']
    print
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price' : price_id,
                        'quantity' : 1,
                        
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


