from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Textile, Cart, Checkout, Coupon
from .forms import TextileForm
from django.contrib import messages
from datetime import datetime


def index(request):
    obj1 = Textile.objects.all()
    return render(request, 'index.html', {'ob': obj1})


def get_us(user):
    a = User.objects.filter(username=user)
    return a[4]


def oneitem(request, id):
    ob = get_object_or_404(Textile, id=id)
    p = ob.price

    if request.method == 'POST':
        u = request.user
        d = datetime.now()
        q = request.POST['quantity']
        s = request.POST['size']
        t = int(q) * int(p)
        messages.info(request, t)

        cart = Cart.objects.create(title_id=ob.id, user_id=u.id, quantity=q, total_price=t, date=d, size=s)
        cart.save()
        obj = Cart.objects.filter(user_id=u.id)
        return render(request, 'cart.html', {'ob': obj})
    return render(request, 'oneob.html', {'ob': ob})


def delete(request, id):
    d = Textile.objects.get(id=id)
    d.delete()
    return render(request, 'index.html')


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
            return render(request, 'index.html')
        else:
            return HttpResponse('invalid login')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


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
                return render(request, 'index.html')
        else:
            messages.info(request, 'Incorrect Password')
            return render(request, 'registration.html')
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
                return render(request, 'index.html')
        else:
            return HttpResponse('Incorrect Password')
    return render(request, 'registration.html')


def search(request):
    if request.method == 'GET':
        prdname = request.GET['search']
        print(prdname)
        status = Textile.objects.filter(title__icontains=prdname)
        if status:
            return render(request, 'search.html', {'ob': status})
        else:
            messages.info(request, 'not available')
            return render(request, 'index.html')
    return render(request, 'index.html')


def searchitem(request, id):
    ob = get_object_or_404(Textile, id=id)
    return render(request, 'searchitem.html', {'ob': ob})


def blog(request):
    return render(request, 'blog.html')


def cart(request):
    ob = request.user
    obj = Cart.objects.filter(user_id=ob.id)
    return render(request, 'cart.html', {'ob': obj})


def checkout(request, id):
    ob = request.user
    obj = Cart.objects.get(title_id=id, user_id=ob.id)
    print(obj.id)

    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        state = request.POST['state']
        town = request.POST['town']
        street = request.POST['street']
        apartment = request.POST['apartment']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        check = Checkout.objects.create(user_id=ob.id, title_id=id, firstname=fname, lastname=lname, state=state, town=town, street=street, apartment=apartment, email=email, postcode=postcode, phone=phone)
        check.save()

        c = request.POST['coupon']
        co = Coupon.objects.get(code=c)
        print(co.cprice)
        if c:
            if Coupon.objects.filter(code=c).exists():
                return render(request, 'checkout.html', {'ob': obj, 'co': co})
            else:
                return HttpResponse('invalid')
        else:
            return HttpResponse('no coupon code')

    return render(request, 'checkout.html', {'ob': obj})


def delete_cart(request, id):
    d = get_object_or_404(Cart, id=id)
    d.delete()
    ob = request.user
    obj = Cart.objects.filter(user_id=ob.id)
    return render(request, 'cart.html', {'ob': obj})


# def coupon(request):
#     co = Coupon.objects.all()
#     print(co)
#     if request.method == 'POST':
#         c = request.POST['coupon']
#         # if Coupon.objects.filter(code=c).exists():
#         for i in co:
#             if i.code == c:
#                 rs = i.cprice
#                 print(rs)
#                 return HttpResponse('valid')
#             else:
#                 return HttpResponse('invalid coupon')
#             endif
#         endfor
