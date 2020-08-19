from . import views
from django.urls import path


urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('confirmation/<subscription_id>',
         views.confirmation, name='confirmation'),

]
