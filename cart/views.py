from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from cart.models import Cart
from clubs.models import Club

@csrf_exempt
def pay(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "physioboost21@gmail.com",
        "amount": "100",
        "item_name": "Complete Physioboost  Package",
        "invoice": "11",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('cart:done')),
        "cancel_return": request.build_absolute_uri(reverse('cart:canceled')),
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "cart/payment.html", context)

def payment_done(request):
    cart = Cart(club_id=Club(request.user.club_id), order_number=122)
    cart.save()
    return render(request, 'cart/done.html')


def payment_canceled(request):
    return render(request, 'cart/canceled.html')