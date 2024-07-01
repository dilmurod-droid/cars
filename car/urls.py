from django.urls import path

from car.views import Home, CarDetailAndBookingView, Create

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('elonberish/', Create.as_view(), name="create"),
    path('detail/<int:pk>/',CarDetailAndBookingView.as_view(),name="detail")
]