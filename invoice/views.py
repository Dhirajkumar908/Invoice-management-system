from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import InvoiceForm
# Create your views here.
def index(request):
    datas=Invoice.objects.all()
    return render(request, 'index.html', {'datas':datas})

# displya invoice function one single invoice to download
def invoice(request,id):
    clintt = User.objects.get(id=id)
    invoice = Invoice.objects.filter(Client_details=clintt).values('Client_details__username','product_details__product_name','price',
                                                                   'quantity','discount','product_details__product_discription')
    return render(request, 'invoic.html',{'invoice':invoice})


# create_invoice function start here
def create_invoice(request):
    if request.method=='POST':
        Client_details_id=request.POST.get('Client_details')
        Client_details=User.objects.get(id=Client_details_id)

        product_details_id=request.POST.get('product_details')
        product_details=Product.objects.get(id=product_details_id)

        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        discount=request.POST.get('discount')
        sub_total=request.POST.get('sub_total')
        invoice=Invoice(Client_details=Client_details,product_details=product_details,price=price,quantity=quantity,discount=discount,sub_total=sub_total)
        invoice.save()
        return redirect ('index')
    users=User.objects.all().exclude(is_superuser=True)
    product=Product.objects.all()
    return render(request, 'invoice_Form.html', {'users':users, 'product':product})

# add_product function   
def add_product(request):
    if request.method=='POST':
        product=request.POST.get('product')
        product_discription=request.POST.get('product_discription')
        product=Product(product_name=product, product_discription=product_discription)
        product.save()
        return redirect('add_product')  
    product=Product.objects.all()
    return render(request,"add_product.html", {'product':product})


#client function to create and list the customer
def client(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        number=request.POST.get('number')
        pincod=request.POST.get('pincode')
        state=request.POST.get('state')
        city=request.POST.get('city')
        Strite=request.POST.get('strite')
        user=User(username=username, email=email,number=number, pincod=pincod,state=state,city=city,Strite=Strite)        
        user.save()
        return redirect('client')
    users=User.objects.all()
    return render(request, 'client.html', {'users':users})
    



def userinvoicedata(request):
    invoicedata=list(Invoice.objects.filter(Client_details=2)).values()

    return HttpResponse('data')


