from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, DeliveryPerson
from django.contrib.auth.decorators import login_required

@login_required
def track_order(request, order_id):
    order = Order.objects.get(id=order_id)
    data = {
        'status': order.status,
        'delivery_person': order.delivery_person.name if order.delivery_person else None,
    }
    return JsonResponse(data)

def home(request):
    # Example personalized home view
    user = request.user
    recommended_products = ... # Logic to fetch personalized items
    return render(request, 'store/home.html', {'recommended_products': recommended_products})