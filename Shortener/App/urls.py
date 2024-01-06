from django.urls import path
from . import views
# from .views import url_shortener,redirect_original

urlpatterns = [
    path('',views.url_shortener,name='url_shortener'),
    path('<str:short_url>/',views.redirect_original,name='redirect_original'),

]