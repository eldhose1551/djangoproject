from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Textile
from .forms import TextileForm
from django.contrib import messages
from .models import Cart, Buynow, Coupon
from .models import datetime


# from .forms import CartForm


def index(request):
    obj1 = Textile.objects.all()
    return render(request, 'index.html', {'ob': obj1})


# def addcart(request, id):
#     form = CartForm(request.POST or None, request.FILES or None)
#     if form_is_valid():
#         # form.instance.author = get_user(request.user)
#         # quantity=request.POST.get('quantitty', '')
#         # obj=Cart(quantity=quantity)
#         # obj.save()
#         form.save()
#         form = CartForm
#     context = {'form': form}
#     return render(request, 'cart.html', context)


def cart(request, id):
    ob = get_object_or_404(Textile, id=id)
    print(id)
    return render(request, 'oneob.html', {'ob': ob})


#
#
# def remove_from_cart(request, id):
#     product = Textile.objects.get(id=id)
#     cart = Cart(request)
#     cart.remove(product)


def oneitem(request, id):
    ob = get_object_or_404(Textile, id=id)

    if request.method == 'POST':
        quantity = request.POST['quantity']
        size = request.POST['size']
        user = request.user
        totalprice = request.POST['totalprice']
        cart = Cart.objects.create(title_id=ob.id, user_id=user.id, quantity=quantity, size=size, date=datetime.now(),
                                   totalprice=totalprice)
        cart.save()
        return redirect('index')
    #     form = CartForm(request.POST or None, request.FILES or None)
    #     return render(request, 'oneob.html', {'ob': ob, 'form': form})
    # form = ''
    return render(request, 'oneob.html', {'ob': ob})


def delete(request, id):
    d = Textile.objects.get(id=id)
    d.delete()
    return redirect('index')


def add(request):
    form = TextileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TextileForm()
    contex = {'form': form}
    return render(request, 'form.html', contex)


def log(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['passwd']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('invalid login')


def logout_view(request):
    logout(request)
    return redirect('index')


def registration(request):
    if request.method == 'POST':
        uname = request.POST['create_username']
        psw = request.POST['create_password']
        cnfrmpsw = request.POST['cnfrm_pswd']
        eid = request.POST['email_create']
        # print(uname)
        if psw == cnfrmpsw:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username already exist..!')
            elif User.objects.filter(email=eid).exists():
                messages.info(request, 'Email already exist..!')
            else:
                user = User.objects.create_user(username=uname, password=psw, email=eid)
                user.save()
                return redirect('index')
        else:
            messages.info(request, 'Incorrect Password')
            return redirect('registration')
    return render(request, 'registration.html')


def reg(request):
    if request.method == 'POST':
        uname = request.POST['create_username']
        psw = request.POST['create_password']
        cnfrmpsw = request.POST['cnfrm_pswd']
        eid = request.POST['email_create']
        # print(uname)
        if psw == cnfrmpsw:
            if User.objects.filter(username=uname).exists():
                return HttpResponse('Username already exist..!')
            elif User.objects.filter(email=eid).exists():
                return HttpResponse('Email already exist..!')
            else:
                user = User.objects.create_user(username=uname, password=psw, email=eid)
                user.save()
                return redirect('index')
        else:
            return HttpResponse('Incorrect Password')
    return render(request, 'registration.html')


def search(request):
    if request.method == 'GET':
        prdname = request.GET['search']
        print(prdname)
        # if Textile.objects.filter(title=prdname):
        #     ob = Textile.objects.filter(title=prdname)
        #     return render(request, 'search.html', {'ob': ob})
        status = Textile.objects.filter(title__icontains=prdname)
        if status:
            return render(request, 'search.html', {'ob': status})
        else:
            messages.info(request, 'not available')
            return redirect('index')
    return redirect('index')


def searchitem(request, id):
    ob = get_object_or_404(Textile, id=id)
    return render(request, 'searchitem.html', {'ob': ob})


def blog(request):
    return render(request, 'blog.html')


def shop(request):
    return render(request, 'shop.html')


def cart1(request):
    ob = request.user
    obj = Cart.objects.filter(user_id=ob.id)
    return render(request, 'cart.html', {'ob': obj})


def removecart(request, id):
    d = get_object_or_404(Cart, id=id)
    d.delete()
    ob = request.user
    obj = Cart.objects.filter(user_id=ob.id)
    return render(request, 'cart.html', {'ob': obj})


def buynow(request, id):
    ob = request.user
    obj = Cart.objects.filter(title_id=id)
    obj1 = Cart.objects.filter(user_id=ob.id)
    if request.method == 'POST':
        firstname = request.POST['first-name']
        street = request.POST['street']
        lastname = request.POST['last-name']
        email = request.POST['emailid']
        state = request.POST['state']
        town = request.POST['town']
        apartment = request.POST['apartment']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        buy = Buynow.objects.create(firstname=firstname, lastname=lastname, state=state, email=email, town=town,
                                    street=street, apartment=apartment, postcode=postcode, phone=phone, user_id=ob.id,
                                    title_id=id)
        buy.save()
        c = request.POST['coupon']
        co = Coupon.objects.get(code=c)
        if c:
            if Coupon.objects.filter(code=c).exists():
                return render(request, 'buynow.html', {'ob': obj, 'co': co})
            else:
                return HttpResponse('not valid')
        else:
            return HttpResponse('not code')

        return render(request, 'buynow.html', {'ob': obj1})

    return render(request, 'buynow.html', {'ob': obj})

# def savebuynow(request):
#     ob = request.user
#     obj = Cart.objects.filter(title_id=ob.id)
#     obj1 =Cart.objects.filter(user_id=ob.id)
#     if request.method == 'POST':
#         firstname = request.POST['first-name']
#         street = request.POST['street']
#         lastname = request.POST['last-name']
#         email = request.POST['emailid']
#         state = request.POST['state']
#         town = request.POST['town']
#         apartment = request.POST['apartment']
#         postcode = request.POST['postcode']
#         phone = request.POST['phone']
#         buy = Buynow.objects.create(firstname=firstname, lastname=lastname, state=state, email=email, town=town,
#                                     street=street, apartment=apartment, postcode=postcode, phone=phone, user_id=ob.id, title_id=id)
#         buy.save()
