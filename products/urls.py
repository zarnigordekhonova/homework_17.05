from django.urls import path
from products.views import *

app_name = 'Products'
urlpatterns = [
    path('books/', BookListView.as_view(), name='BookListView'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail-view'),
    path('create/', BookCreateView.as_view(), name='create-book'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete-book'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update-book'),
    path('reviews/<int:pk>', get_reviews, name='get-review'),
    path('review/detail/<int:pk>', review_detail, name='review-detail'),
    path('add_review/<int:pk>',add_review, name='add-review')

]