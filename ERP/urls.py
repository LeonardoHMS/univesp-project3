from django.contrib import admin
from django.urls import include, path

from .views import login_page, logout_view, products_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # Frontend
    path('login/',    login_page,    name='login'),
    path('register/', register_page, name='register'),
    path('logout/',   logout_view,   name='logout'),
    path('products/', products_page, name='products'),
    # API
    path('api/', include('warehouse.urls')),
]
