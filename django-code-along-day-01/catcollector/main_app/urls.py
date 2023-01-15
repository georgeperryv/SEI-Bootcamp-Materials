from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    # http://localhost:8000/about-us/
    path('about-us/', views.about_us, name='about_us'),
    # http://localhost:8000/cats/
    path('cats/', views.cat_index, name='index'),
    # http://localhost:8000/cats/1/
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # new route used to show a form and create a cat.
    # http://localhost:8000/cats/create/
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    # http://localhost:8000/cats/2/update/
    path('cats/<int:pk>/update/',
         views.CatUpdate.as_view(), name='cats_update'),
    # http://localhost:8000/cats/2/delete/
    path('cats/<int:pk>/delete/',
         views.CatDelete.as_view(), name='cats_delete'),
    # http://localhost:8000/cats/2/add_feeding/
    path('cats/<int:cat_id>/add_feeding/',
         views.add_feeding, name="add_feeding"),

    # http://localhost:8000/cats/2/assoc_toy/1/
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/',
         views.assoc_toy, name="assoc_toy"),
    path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),

    # http://localhost:8000/toys/
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    # http://localhost:8000/toys/1/
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # http://localhost:8000/toys/create/
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    # http://localhost:8000/toys/1/update/
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    # http://localhost:8000/toys/1/delete/
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    # http:///localhost:8000/accounts/signup/
    path('accounts/signup/', views.signup, name='signup'),
]
