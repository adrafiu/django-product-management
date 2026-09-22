from django.shortcuts import render, redirect
from .models import ProductModel


def home(request):
    return render(request, "home.html")


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        production_date = request.POST.get("production_date")

        ProductModel.objects.create(
            name=name,
            description=description,
            price=price,
            production_date=production_date,
            image=request.FILES.get("image")
        )

        return redirect("product_list")

    return render(request, "add_product.html")


def product_list(request):
    products = ProductModel.objects.all()

    filtered_products = ProductModel.objects.filter(
        price__gte=100
    )

    context = {
        "products": products,
        "filtered_products": filtered_products
    }

    return render(
        request,
        "product_list.html",
        context
    )


def update_product(request, product_id):
    product = ProductModel.objects.get(id=product_id)

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.production_date = request.POST.get("production_date")

        if request.FILES.get("image"):
            product.image = request.FILES.get("image")

        product.save()

        return redirect("product_list")

    products = ProductModel.objects.all()

    filtered_products = ProductModel.objects.filter(
        price__gte=100
    )

    context = {
        "products": products,
        "filtered_products": filtered_products,
        "product": product,
        "edit_mode": True
    }

    return render(
        request,
        "product_list.html",
        context
    )
    
def delete_product(request, product_id):
    product = ProductModel.objects.get(id=product_id)
    product.delete()
    return redirect("product_list")    