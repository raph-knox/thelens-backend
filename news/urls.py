from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
