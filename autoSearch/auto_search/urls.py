from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = "Home"),
    path('open_edge/', views.open_edge, name = 'open_edge'),
    path('search/',views.search, name = 'search'),
    path('search_mobile/', views.search_mobile, name = 'search_mobile'),
]
