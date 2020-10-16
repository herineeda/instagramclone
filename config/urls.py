from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),  #photo의 urls include 통해 연결
    path('accounts/', include('accounts.urls')),
]
