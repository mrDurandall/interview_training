from django.shortcuts import render

from django.views.generic import ListView

from .models import Good


class GoodsListView(ListView):
    model = Good
    queryset = Good.on_site.select_related('supplier').prefetch_related().all()
