from django.shortcuts import render
from search.models import Product 

# Create your views here.
def index(request):
    results = Product.objects.all()
    return render(request, 'index.html', {'results': results})
