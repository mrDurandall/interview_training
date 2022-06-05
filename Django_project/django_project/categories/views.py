from django.views.generic import DetailView, ListView


from .models import Category


class CategoryDetailView(DetailView):
    model = Category
    extra_context = {'title': 'Раздел'}


class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'Разделы'}
    queryset = Category.on_site.prefetch_related().all()
