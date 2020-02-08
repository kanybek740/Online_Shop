from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Purchase, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, CartCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage


def product_list(request):
    object_list = Product.objects.all().order_by('-price')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'page': page,
                                        'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.name = request.user
            new_comment.save()
            comment_form=CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, 'product_detail.html', {'product': product,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
@login_required
def cart_list(request):
    carts = Purchase.objects.filter(customer=request.user)
    total = 0
    for i in carts:
        total += i.cost
    # price = Purchase.cost.filter(customer = request.user)
    return render(request, 'cart.html', {'carts': carts,
                                        'total':total})

def about(request):
    return render(request, 'index.html')

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = CartCreationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_cart = form.save(commit=False)
            new_cart.customer = request.user
            new_cart.product = product
            new_cart.save()
            messages.success(request, 'Added')
            return redirect('shop:product_list')
    else:
        form = CartCreationForm(data=request.GET)
        return render(request, 'add_to_cart.html', {'form':form})

def delete_from_cart(request, pk):
    purchase = Purchase.objects.get(pk=pk)
    purchase.delete()
    return redirect('shop:cart_list')

    # class Home(TemplateView):
    # template_name = 'home.html'


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
    return render(request, 'upload.html', locals())
