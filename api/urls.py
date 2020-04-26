from django.urls import path
from api import views
urlpatterns = [
    path('cats/', views.categories),
    path('toys/category/', views.category),

    path('toys/', views.Toys.as_view()),
    path('toys/<int:id>/', views.toy_detailed),

    path('order/', views.order)
]