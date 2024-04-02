from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
# Create your views here.

def list_products(request):
    object = Products.objects.all()

    #search functionality
    item_name = request.GET.get('searched_item')
    if item_name:   
        object = Products.objects.filter(product_title__icontains=item_name)

    #pagination functionality
    paginator = Paginator(object,4)
    page = request.GET.get('page')
    object = paginator.get_page(page)

    return render(request,'index.html',{'product_object':object})

def detail_product(request,product_id):
    object = Products.objects.get(pk=product_id)
    return render(request,'detail.html',{'product_object':object})


def checkout(request):

    if request.method=='POST':
        item = request.POST.get('items',"")
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        state = request.POST.get("state","")
        zip = request.POST.get("zip","")
        total = request.POST.get('total',"")

        order = Order(items=item,name=name,email=email,address=address,city=city,state=state,zip=zip,totalcost=total)
        order.save()
    return render(request,'checkout.html')


