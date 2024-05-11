from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')

class GetTest(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return render(request, 'get_test.html')
