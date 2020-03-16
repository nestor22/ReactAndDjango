
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #no se usara por ahora el panel de administracion
   # path('admin/', admin.site.urls),
   path('', include('leads.urls')),
]


