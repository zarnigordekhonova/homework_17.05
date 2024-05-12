from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, CreateView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views import View
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewsForm
# Create your views here.


class BookListView(View):
    def get(self, request):
        books = Books.objects.all().order_by('-pk')
        context = {
            'books' : books
        }
        return render(request, 'book/get_book.html', context=context)


class BookDetailView(DetailView):
    model = Books
    template_name = 'book/book_detail.html'



class BookCreateView(CreateView):
    model = Books
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('Products:BookListView')


class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book/book_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('Products:BookListView')

class BookUpdateView(UpdateView):
    model = Books
    template_name = 'book/book_update.html'
    fields = '__all__'
    success_url = reverse_lazy('Products:detail-view')

    def get_success_url(self):
        return reverse_lazy('Products:detail-view', kwargs={'pk': self.object.pk})


def get_reviews(request, pk):
    items = Reviews.objects.filter(book=pk)
    context = {
        'items' : items
    }

    return render(request, 'book/reviews.html', context=context)


def review_detail(request, pk):
    item = Reviews.objects.get(pk=pk)
    context = {
        'item' : item
    }
    return render(request, 'book/review_detail.html', context=context)

def add_review(request, pk):
    form = ReviewsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('Products:BookListView')
    context = {
        'form': form
    }
    return render(request, 'book/add_review.html', context=context)
