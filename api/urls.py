from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('cats/', views.categories),
    path('toys/category/', views.category),

    path('toys/', views.Toys.as_view()),
    path('toys/<int:id>/', views.toy_detailed),
    path('login/', obtain_jwt_token),

    path('order/', views.order),
    path('toys/admin/', views.ToyAdmin.as_view()),
    path('toys/admin/<int:id>/', views.deleteToy),
]