from django.urls import path

from .views import (CustomAuthToken, LogoutView, MeasureListCreateView,
                    ProductDetailView, ProductListCreateView,
                    TypeListCreateView, home_view)

urlpatterns = [
     path('', home_view, name='redirect-product'),
     path('api/estoque/',
          ProductListCreateView.as_view(),
          name='product-list-create'),
     path('api/estoque/<int:pk>/',
          ProductDetailView.as_view(),
          name='product-detail'),
     path('api/medida/',
          MeasureListCreateView.as_view(),
          name='measure-list-create'),
     path('api/tipo/',
          TypeListCreateView.as_view(),
          name='type-list-create'),
     path('api/login/',
          CustomAuthToken.as_view(),
          name='api-login'),
     path('api/logout/',
          LogoutView.as_view(),
          name='api-logout')
]
