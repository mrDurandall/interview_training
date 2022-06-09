from django.urls import path


from .views import CategoryListView, CategoryDetailView


app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category'),
]