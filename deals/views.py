from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Deal
from .forms import DealForm


def deal_table(request):
    deals = Deal.objects.all()
    return render(request, 'deals/deal_table.html', {'deals': deals})


def deal_detail(request, pk):
    deal = get_object_or_404(Deal, pk=pk)
    return render(request, 'deals/deal_detail.html', {'deal': deal})


def deal_new(request):
    form = DealForm()
    return render(request, 'deals/deal_edit.html', {'form': form})