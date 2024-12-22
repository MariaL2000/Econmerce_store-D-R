from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
#from Users.views import HomeView

schema_view = get_schema_view(title='Ecommerce API')

urlpatterns = [
   # path('', HomeView.as_view(), name='home'),  # Servir la aplicación React desde la raíz
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('products/', include('Products.urls')),
    path('car/', include('Car_list.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='Ecommerce API')),
    path('schema/', schema_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)