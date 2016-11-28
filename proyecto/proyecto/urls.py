from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'inventario/', include('inventario.urls')),
    url(r'^admin/', admin.site.urls),
]
