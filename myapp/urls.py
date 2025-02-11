# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی اپلیکیشن
    path('about/', views.about, name='about'),  # صفحه درباره ما
    path('contact/', views.contact, name='contact'),  # صفحه تماس با ما
]
