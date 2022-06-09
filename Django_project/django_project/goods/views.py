from django.shortcuts import render

from django.views.generic import ListView

from .models import Good


class GoodsListView(ListView):
    model = Good
    queryset = Good.objects.select_related('supplier').prefetch_related().all()
