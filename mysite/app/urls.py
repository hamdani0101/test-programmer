from django.urls import path
from . import views

urlpatterns=[
    path('', views.produk_list, name='produk_list'),
    path('produk-bisa-dijual/', views.produk_bisa_dijual, name='produk_bisa_dijual'),
    path('tambah-produk/', views.produk_tambah, name='produk_tambah'),
    path('edit-produk/<int:id>/', views.produk_edit, name='produk_edit'),
    path('hapus-produk/<int:id>/', views.produk_hapus, name='produk_hapus'),
    path('import-produk/', views.import_produk),
]