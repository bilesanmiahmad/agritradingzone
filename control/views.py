from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from trades import models as mt
from accounts import models as ma


# Create your views here.


@login_required()
def add_crop(request):
    if request.method == 'POST':
        if request.POST['name']:
            crop = mt.Crop.objects.create(name=request.POST['name'])
            return redirect('crops')
    else:
        return render(request, 'control/add-crop.html')


@login_required()
def edit_crop(request, crop_id):
    if request.user.is_rahman:
        crop = mt.Crop.objects.get(id=crop_id)
        if request.method == 'POST':
            if request.POST['name']:
                crop.name = request.POST['name']
                crop.save()
        else:
            return render(request, 'control/edit-crop.html', {'crop': crop})
    return redirect('products')


@login_required()
def delete_crop(request, crop_id):
    if request.user.is_rahman:
        crop = mt.Crop.objects.get(id=crop_id)
        if request.method == 'POST':
            if request.POST['name']:
                crop.delete()
        else:
            return redirect('crops')
    return redirect('products')


@login_required()
def list_crops(request):
    if not request.user.is_rahman:
        return redirect('products')

    crops = mt.Crop.objects.all()
    return render(request, 'control/crops.html', {'crops': crops})


@login_required()
def add_product(request):
    if not request.user.is_rahman:
        return redirect('products')

    crops = mt.Crop.objects.all()
    if request.method == 'POST':
        if (request.POST['crop'] and request.POST['qty']
            and request.POST['type']
            and request.POST['method']
            and request.POST['details']
            and request.POST['price']
            and request.POST['metric']):
            crop = mt.Crop.objects.get(id=int(request.POST['crop']))
            product = mt.Product()
            product.crop = crop
            product.prod_type = request.POST['type']
            product.method = request.POST['method']
            product.quantity = int(request.POST['qty'])
            product.image = request.FILES['img']
            if request.POST['proddate'] == '' and request.POST['expdate'] == '':
                product.prod_date = None
                product.exp_date = None
            else:
                pdate = datetime.strptime(request.POST['proddate'], "%m/%d/%Y")
                edate = datetime.strptime(request.POST['proddate'], "%m/%d/%Y")
                product.prod_date = datetime.strftime(pdate, "%Y-%m-%d")
                product.exp_date = datetime.strftime(edate, "%Y-%m-%d")
            product.details = request.POST['details']
            product.price = float(request.POST['price'])
            product.metric = request.POST['metric']
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'control/add-product.html', {
                'errors': 'Fill in the required fields',
                'crops': crops
            })
    else:
        return render(request, 'control/add-product.html', {'crops': crops})


@login_required()
def details(request, product_id):
    product = get_object_or_404(mt.Product, pk=product_id)
    return render(request, 'control/product-detail.html', {'product': product})
