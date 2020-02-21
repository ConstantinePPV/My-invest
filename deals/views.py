from django.shortcuts import render
from django.utils import timezone
from .models import Deal

def deal_table(request):
    deals = Deal.objects.all()
    return render(request, 'deals/deal_table.html', {'deals': deals})