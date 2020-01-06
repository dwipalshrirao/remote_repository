from django.http import HttpResponse
from django.shortcuts import render
from curdapp.forms import updatingdataform,insertingDataform,deletingdataform,retrive_dataform
from curdapp.models import productdata

def homeview(request):
	return render(request,"curd_home.html")

def create(request):
	if request.method == 'POST':
			product_id=request.POST.get('pid')
			product_name=request.POST.get('pname')
			product_class=request.POST.get('pclass')
			product_cost=request.POST.get('pcost')
			no_of_product=request.POST.get('pnop')
			manufacturare_date=request.POST.get('pmdate')
			expirydate=request.POST.get('pedate')
			customer_name=request.POST.get('cname')
			mobile=request.POST.get('mobile')
			Email=request.POST.get('email')
			data=productdata(
				product_id=product_id,
				product_name=product_name,
				product_class=product_class,
				product_cost=product_cost,
				no_of_product=no_of_product,
				manufacturare_date=manufacturare_date,
				expirydate=expirydate,
				customer_name=customer_name,
				mobile=mobile,
				Email=Email
			)
			data.save()
			return render(request, "curd_home.html")
	else:
		return render(request,"insert_form.html")

def retrieve(request):
	pdata=productdata.objects.filter()
	return render(request,'retrieve_file.html',{'pdata':pdata})

def update(request):
	if request.method=="POST":
		product_id1=request.POST.get('pid')
		product_cost1=request.POST.get('pcost')
		pdata=productdata.objects.filter(product_id=product_id1)

		if not pdata:
			return HttpResponse("Product ID Not Available")
		else:
			pdata.update(product_cost=product_cost1)
			return render(request,"update_form.html")
	else:
		return render(request,'update_form.html')


def delete(request):
	if request.method=="POST":
		product_id1=request.POST.get('pid')
		data=productdata.objects.filter(product_id=product_id1)
		if not data:
			return HttpResponse("Product ID Not Available")
		else:
			data.delete()
			return render(request,'delete_form.html')
	else:
		return render(request,'delete_form.html')