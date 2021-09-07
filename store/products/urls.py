from django.urls import path
from .views import home, product_upload_view , delete_product, edit_product, Addcategory
urlpatterns = [
    path('', home, name='all-products'),
    path('upload/', product_upload_view , name='add-products'),
    path ('delete/<product_id>', delete_product, name='delete_product'),
    path ('edit/<int:pk>', edit_product.as_view(), name='edit_product'),
    path('cat/', Addcategory.as_view(),name='add-category')
]