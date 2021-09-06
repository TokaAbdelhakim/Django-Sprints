from django.shortcuts import redirect, render
from .models import Product
from .forms import  PostForm, EditForm
from django.views.generic import UpdateView
# Create your views here.
def home (request):
    products = Product.objects.all()
    return render (request, 'products.html',{
        'all_products' : products
    })

def product_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            showme = 1 if ('showme' in request.POST) else 0
            form.save()
            # Get the current instance object to display in the template
            #img_obj = form.instance
            #return render (request,'add.html',{'form':form, 'img_obj': img_obj})
            return redirect ('all-products')
    else:
        form = PostForm()
    return render(request, 'add.html', {'form':form})

def delete_product(request,product_id):
    Product.objects.get(pk=product_id).delete()

    return redirect('all-products')

class edit_product (UpdateView):
    model = Product
    #fields = ['name', 'description', 'image', 'price','category']
    form_class = EditForm
    template_name = 'edit.html'
    


''''
 def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_photo = request.POST.get('product_photo')
        product_price = request.POST.get('product_price')
        Product.objects.create(
                name = product_name,
                description = product_description,
                image = product_photo,
                price = product_price
            )
'''