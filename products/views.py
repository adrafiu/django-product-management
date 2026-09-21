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
            production_date=production_date
        )

        return redirect("product_list")

    return render(request, "add_product.html")


def product_list(request):
    products = ProductModel.objects.all()

    return render(
        request,
        "product_list.html",
        {"products": products}
    )