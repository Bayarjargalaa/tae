from django.urls import path
from . import views


urlpatterns = [
    path('', views.consql, name='home'),
    path('items/', views.items_view, name='items'),
    path('image/', views.items_view_image, name='image'),
    path('tail/', views.import_excel_to_db, name='tail'),
    path('contact/', views.import_excel_to_db, name='contact'),
    # path('product_list/', views.product_list, name='product_list'),
    path('views/', views.show_views, name='views'),
    
]
