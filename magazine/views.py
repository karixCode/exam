from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .models import Product, Order

from .forms import RegisterForm

# Create your views here.

def index(request):
    products = Product.objects.all()[:5]
    return render(request, 'index.html', {'products': products})

class ServiceListView(ListView):
    model = Product
    template_name = 'magazine/service_list.html'

class ServiceDetailView(DetailView):
    model = Product
    template_name = 'magazine/service_detail.html'

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        Order.objects.create(user=request.user, product=product)
        return redirect('profile')

def logout_view(request):
    logout(request)
    return redirect('index')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@login_required
def profile(request):
    return render(request, 'magazine/profile.html')

def search_result(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query) if query else None
    return render(request, 'magazine/search_result.html', {'products': products, 'query': query})
