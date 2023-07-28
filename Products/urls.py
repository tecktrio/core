from django.urls import path
from .views import GetAllProducts,UploadProduct,HandleUserProducts

urlpatterns = [
    path('GetAllProducts',GetAllProducts.as_view()),
    path('UploadProduct',UploadProduct.as_view()),
    path('HandleUserProducts/<str:Email>',HandleUserProducts.as_view()),
    path('HandleUserProducts',HandleUserProducts.as_view())
]