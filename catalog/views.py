from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Product, CategoriesSecond, CategoriesFirst, Brand, Order
from cart.cart import Cart
from django.http import HttpResponseRedirect
import random
from django.db.models import Q
def index(request):
    brands = Brand.objects.all()[:15]
    popular = Product.objects.all().order_by('-views')[:15]
    products = Product.objects.all()

    categoryes = return_category()
    cart = Cart(request)
    context = {'products':products, 'category_1':categoryes['category_1'], 'category_2':categoryes['category_2'],
               'category_3':categoryes['category_3'], 'cart':cart, 'brands':brands, 'popular':popular}
    return render(request, "catalog/index.html", context)

def item(request, id):
    brands = Brand.objects.all()[:15]
    popular = Product.objects.all().order_by('-views')[:15]
    cart = Cart(request)
    randQuery = Product.objects.order_by('?')[:4]
    categoryes = return_category()
    item = get_object_or_404(Product, id = id)
    item.views += 1
    item.save()
    category = CategoriesSecond.objects.get(name = item.category)
    section = CategoriesFirst.objects.get(name = category.section)
    cart_product_form = CartAddProductForm()
    context = {'item':item, 'cart_product_form':cart_product_form, 'category': category, 'section':section,'category_1':categoryes['category_1'], 'category_2':categoryes['category_2'],
               'category_3':categoryes['category_3'], 'randquery':randQuery, 'cart':cart, 'brands':brands, 'popular':popular}
    return render(request, "catalog/item.html", context)

def category(request, slug):
    brands = Brand.objects.all()[:15]
    popular = Product.objects.all().order_by('-views')[:15]
    cart = Cart(request)
    category = CategoriesSecond.objects.get(slug = slug)
    section = CategoriesFirst.objects.get(name = category.section)
    products = Product.objects.filter(category = category)
    categoryes = return_category()
    context = {'category':category, 'products':products,'category_1':categoryes['category_1'], 'category_2':categoryes['category_2'],
               'category_3':categoryes['category_3'], 'section':section, 'cart':cart, 'brands':brands, 'popular':popular}
    return render(request, "catalog/catalog.html", context)

def brand(request, slug):
    brands = Brand.objects.all()[:15]
    popular = Product.objects.all().order_by('-views')[:15]
    brand = Brand.objects.get(slug = slug)
    products = Product.objects.filter(brand = brand)
    cart = Cart(request)
    categoryes = return_category()
    context = {'cart':cart, 'products' : products, 'brand' : brand, 'brands':brands, 'popular':popular}
    return render(request, "catalog/catalog.html", context)
def return_category():
    woman = CategoriesFirst.objects.get(name = "Женщинам")
    man = CategoriesFirst.objects.get(name = "Мужчинам")
    kid = CategoriesFirst.objects.get(name = "Детям")
    category_1 = CategoriesSecond.objects.filter(section = woman)
    category_2 = CategoriesSecond.objects.filter(section = man)
    category_3 = CategoriesSecond.objects.filter(section = kid)
    categoryes = {'category_1':category_1, 'category_2':category_2, 'category_3':category_3}
    return categoryes

def search(request):
    brands = Brand.objects.all()[:15]
    popular = Product.objects.all().order_by('-views')[:15]
    cart = Cart(request)
    categoryes = return_category()
    if request.method == "POST":
        q = request.POST['q']
        result = Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(description__iexact=q) | Q(name__icontains=q.title()))
        context = {'result':result,'category_1':categoryes['category_1'], 'category_2':categoryes['category_2'],
                   'category_3':categoryes['category_3'], 'q' : q, 'cart':cart, 'brands':brands, 'popular':popular}
        return render(request, "catalog/search.html", context)
    else:
        context = {'category_1':categoryes['category_1'], 'category_2':categoryes['category_2'],
                   'category_3':categoryes['category_3'], 'cart':cart, 'brands':brands, 'popular':popular}
        return render(request, "catalog/search.html", context)

def order(request):
    brands = Brand.objects.all()[:15]
    popular = Product.objects.all().order_by('-views')[:15]
    products = Product.objects.all()
    categoryes = return_category()
    cart = Cart(request)
    context = {'products':products, 'category_1':categoryes['category_1'], 'category_2':categoryes['category_2'],
               'category_3':categoryes['category_3'], 'cart':cart, 'brands':brands, 'popular':popular}
    if request.method == "POST":
        order = Order()
        order.last_name = request.POST['last_name']
        order.first_name = request.POST['first_name']
        order.two_name = request.POST['two_name']
        order.phone = request.POST['phone']
        order.stat = request.POST['stat']
        order.street = request.POST['street']
        order.house = request.POST['house']
        order.index = request.POST['index']
        order.att = request.POST['att']
        order.product = request.POST['product']
        order.save()
        return render(request, "catalog/thank.html", context)
