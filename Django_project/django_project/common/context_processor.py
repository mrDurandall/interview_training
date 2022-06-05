from categories.models import Category


def navbar_categories(request):
    return {'categories_list': Category.on_site.all()}


def sitename(request):
    return {'sitename': request.site.name}
