from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('news.urls')), 
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token),
]

