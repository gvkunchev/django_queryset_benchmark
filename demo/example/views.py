import inspect

from time import perf_counter

from django.views import View
from django.shortcuts import render

from .models import Supplier, Product


class Timed:

    def __init__(self):
        self._duration = None

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, *_):
        self._duration = perf_counter() - self._start

    def __str__(self):
        return str(self._duration)


class IndexView(View):

    def __init__(self):
        self._iter_index = 0

    @staticmethod
    def method1(supplier_name):
        """Naive approach."""
        products = Product.objects.all()
        result = []
        for product in products:
            if product.quantity >= 20:
                continue
            if product.supplier.name == supplier_name:
                result.append(product)
        return result

    @staticmethod
    def method2(supplier_name):
        """Naive approach."""
        return Product.objects.filter(supplier__name=supplier_name, quantity__lt=20)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self._iter_index += 1
            return getattr(self, f'method{self._iter_index}')
        except AttributeError:
            raise StopIteration

    def get(self, request):
        supplier_name = Supplier.objects.get(pk=1).name
        methods = []
        for method in self:
            with Timed() as timer:
                result = method(supplier_name)
            methods.append({
                    'definition': inspect.getsource(method),
                    'timer': timer
            })
        context = {
            'methods': methods,
            'products_count': len(Product.objects.all()),
            'match_count': len(result)
        }
        return render(request, 'index.html', context)
