import stripe
import logging
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWebhookHandler

# Initialize logger
logger = logging.getLogger(__name__)

@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    # Setup Stripe keys
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', None)

    if not sig_header:
        logger.error("Stripe signature header missing")
        return HttpResponse("Missing signature header", status=400)

    event = None

    try:
        # Verify webhook signature
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
        logger.info("Webhook received: %s", event['type'])
    except ValueError as e:
        logger.error("Invalid payload: %s", e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error("Signature verification failed: %s", e)
        return HttpResponse(status=400)
    except Exception as e:
        logger.error("Error constructing webhook event: %s", e)
        return HttpResponse(status=500)

    # Initialize the webhook handler
    handler = StripeWebhookHandler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Get the event type from the Stripe event
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the appropriate handler function
    try:
        response = event_handler(event)
        logger.info("Event %s handled successfully.", event_type)
        return response
    except Exception as e:
        logger.error("Error handling event %s: %s", event_type, e)
        return HttpResponse(status=500)
