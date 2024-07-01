from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from car.models import Car, Booking
from users.forms import UserRegisterForm
from users.models import CustomUser


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'registration/login.html')
        else:
            return render(request, 'registration/login.html')


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        return super().form_valid(form)
class Profile(LoginRequiredMixin,ListView):
    model = Booking
    template_name = 'profile.html'
    context_object_name = 'cars'

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(CustomUser, username=username)
        return Booking.objects.filter(user=user)