from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Assets, BorrowTransaction, CATEGORY
from .forms import AssetsForm, BorrowForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.db.models import Case, When, Value, BooleanField, Count, Q
# Create your views here.

@login_required(login_url='user-login')
def index(request):
    borrow = BorrowTransaction.objects.all().filter(date_returned=None)
    if request.method=='POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            name = form.cleaned_data.get('asset')
            messages.success(request, f'{name} borrowed!')
            return redirect('dashboard-index')
    else:
        form = BorrowForm()
    context = {
        'borrow': borrow,
        'form': form
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff.html', context)

@login_required(login_url='user-login')
def staff_details(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff_details.html', context)

@login_required(login_url='user-login')
def assets(request):
    #all_assets = Assets.objects.all()

    if request.method == 'POST':
        form = AssetsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = AssetsForm()
    all_assets = Assets.objects.all().order_by('category')
    '''filter_category = request.GET.get('category')
    chart_data = Assets.objects.all()
    if filter_category:
        chart_data = chart_data.filter(category=filter_category)

    total_assets = chart_data.count() 
    borrowed_unreturned_assets = BorrowTransaction.objects.filter(
        date_returned=None,  
        asset__in=chart_data  # Only borrow records related to current data 
    ).count() '''

    context = {
        'all_assets': all_assets,
        'form': form,
        #'total assets': total_assets,
        #'borrowed_unreturned_assets': borrowed_unreturned_assets,
        'categories': CATEGORY
    }
    return render(request, 'dashboard/assets.html', context)

def calculate_chart_data(request):
    filter_category = request.GET.get('category')

    data = Assets.objects.all()
    if filter_category:
        data = data.filter(category=filter_category)

    total_assets = data.count()
    borrowed_unreturned_assets = BorrowTransaction.objects.filter(
        date_returned=None,
        asset__in=data
    ).count()

    return JsonResponse({
        'total_assets': total_assets,
        'borrowed_unreturned_assets': borrowed_unreturned_assets,
    })


@login_required(login_url='user-login')
def assets_return(request, pk):
    item = Assets.objects.get(id=pk)
    if request.method=='POST':
        item.date_returned=timezone.now().date()
        item.is_available=True
        item.save()
        borrow_record = BorrowTransaction.objects.get(asset=item, date_returned=None)
        borrow_record.date_returned = timezone.now().date()  
        borrow_record.save()
        return redirect('dashboard-index')
    return render(request, 'dashboard/assets_return.html')

@login_required(login_url='user-login')
def assets_borrow(request):
    if request.method=='POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            asset = form.cleaned_data['asset']
            registration_number = asset.name
            #dateborrowed = form.cleaned_data['date_borrowed']
        #try:
            item = Assets.objects.get(name=registration_number, is_available=True)
            BorrowTransaction.objects.create(asset=item, staff_member=request.user)
            item.is_available = False
            item.save()
            return redirect('dashboard-index')        
        #except Assets.DoesNotExist:
        #    form.add_error(None, 'Asset not found or unavailable')   
    else:
        form = BorrowForm()
    #all_assets = BorrowTransaction.objects.all()
    all_assets = {}
    for transaction in BorrowTransaction.objects.all().order_by('-date_returned'):  
        asset_name = transaction.asset.name
        if asset_name not in all_assets:
            all_assets[asset_name] = [] 
        all_assets[asset_name].append(transaction)
        all_assets[asset_name] = all_assets[asset_name][:1]
    context = {
        'form': form,
        'all_assets': all_assets.values()
    }
    return render(request, 'dashboard/assets_borrow.html', context)