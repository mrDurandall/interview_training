from categories.models import Category


def navbar_categories(request):
    return {'categories_list': Category.objects.all()}

