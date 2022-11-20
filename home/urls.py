from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_review, name='add_review'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('about_us/', views.about_us, name='about_us'),
    path('faq/', views.faq, name='faq'),
]
