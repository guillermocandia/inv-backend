from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static


schema_view = get_swagger_view(title='API')
admin.site.site_header = 'Administración'


urlpatterns = [
    path('', include('app.base.urls')),
    path('', schema_view),
    path('index.html', schema_view),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('inventory/', include('app.inventory.urls')),
    path('', include('app.sales.urls')),
    path('', include('app.report.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
