from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('customer/', include('customer.urls')),
    path('shopkeeper/', include('shopkeeper.urls'))
]
