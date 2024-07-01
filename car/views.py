from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin

from car.forms import CarForm
from car.models import Car, Booking


class Home(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'



class Detail(DetailView):
    model = Car
    template_name = 'detail.html'
    context_object_name = 'car'

class Create(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'elonberish.html'
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class CarBookingView(SingleObjectMixin, View):
        model = Car
        def post(self, request, *args, **kwargs):
            car = self.get_object()
            if not car.available:
                return redirect('detail', pk=car.pk)
            Booking.objects.create(user=request.user, car=car)
            car.available = False
            car.save()
            return redirect('detail', pk=car.pk)
class CarDetailAndBookingView(View):

    def get(self, request, *args, **kwargs):
        view = Detail.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CarBookingView.as_view()
        return view(request, *args, **kwargs)