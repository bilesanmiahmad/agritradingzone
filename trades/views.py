from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from trades import models as mt
from trades import constants as ct
from tradingzone.utils import mail


# Create your views here.


def list_products(request):
    products = mt.Product.objects.filter(is_closed=False)
    return render(
        request,
        'trades/products.html',
        {'products': products})


@login_required()
def add_product(request):
    products = mt.Crop.objects.all()
    if request.method == 'POST':
        pass
    else:
        return render(
            request,
            'trades/products.html',
            context={'product': products})


def close_product(request, product_id=None):
    if request.user.is_rahman:
        product = mt.Product.objects.get(id=product_id)
        product.is_closed = True
        product.save()
        return redirect('products')


@login_required()
def add_bid(request, product_id=None):
    product = mt.Product.objects.get(id=product_id)
    packages = ct.PACKAGES
    if request.method == 'POST':
        if request.POST['weight'] and request.POST['price']:
            bid = mt.Bid()
            bid.product = product
            bid.client = request.user
            bid.package = request.POST['package']
            bid.weight = request.POST['weight']
            bid.price = request.POST['price']
            bid.save()
            mail.send_email()
            return redirect('products')
    else:
        return render(
            request,
            'trades/add-bid.html',
            context={
                'product': product,
                'user': request.user.get_full_name(),
                'packages': packages
            }
        )


def get_bids(request):
    user = request.user
    if user.is_rahman:
        return redirect('all-bids')
    bids = mt.Bid.objects.filter(client=user)
    return render(request, 'trades/bids.html', {'bids': bids})


def get_bid(request, bid_id):
    bid = mt.Bid.objects.get(id=bid_id)
    return render(request, 'trades/bid.html', {'bid': bid})


def accept_bid(request, bid_id):
    if request.user.is_rahman:
        bid = mt.Bid.objects.get(id=bid_id)
        bid.is_accepted = True
        bid.save()
        return redirect('all-bids')
    else:
        return redirect('products')


def deny_bid(request, bid_id):
    if request.user.is_rahman:
        bid = mt.Bid.objects.get(id=bid_id)
        bid.is_accepted = False
        bid.save()
        return redirect('all-bids')
    else:
        return redirect('products')


def all_bids(request):
    if request.user.is_rahman:
        bids = mt.Bid.objects.all()
        return render(request, 'trades/bids.html', {'bids': bids})
    else:
        redirect('products')


@login_required()
def add_sale(request):
    if request.method == 'POST':
        if (request.POST['crop'] and request.POST['qty'] and
            request.POST['metric'] and request.POST['details'] and
            request.POST['price']):
            sale = mt.Sale()
            sale.crop = request.POST['crop']
            sale.seller = request.user
            sale.quantity = request.POST['qty']
            sale.metric = request.POST['metric']
            sale.details = request.POST['details']
            sale.price = request.POST['price']
            sale.save()
            mail.send_email()
            return redirect('sales')
    else:
        return render(
            request,
            'trades/add-sale.html')


@login_required()
def get_sale(request, sale_id):
    sale = mt.Sale.objects.get(id=sale_id)
    return render(request, 'trades/sale-item.html', {'sale': sale})


@login_required()
def get_sales(request):
    user = request.user
    if user.is_rahman:
        return redirect('all-sales')
    sales = mt.Sale.objects.filter(seller=user)
    return render(request, 'trades/sales.html', {'sales': sales})


@login_required()
def all_sales(request):
    if request.user.is_rahman:
        sales = mt.Sale.objects.all()
        return render(request, 'trades/sales.html', {'sales': sales})
    else:
        redirect('products')
