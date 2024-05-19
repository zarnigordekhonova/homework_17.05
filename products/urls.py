from django.urls import path
from products.views import *

app_name = 'Products'
urlpatterns = [
    path('books/', BookListView.as_view(), name='BookListView'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail-view'),
    path('create/', BookCreateView.as_view(), name='create-book'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete-book'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add-review'),
    path('edit_review/<int:pk>', ReviewUpdateView.as_view(), name='edit-review'),
    path('category/', CategoriesListView.as_view(), name='category'),
]