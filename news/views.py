from rest_framework import viewsets, permissions, filters
from .models import Article
from .serializers import ArticleSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only the article's author can edit or delete.
    """

    def has_object_permission(self, request, view, obj):
        # Safe methods (GET, HEAD, OPTIONS) are allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, only the author can edit/delete
        return obj.author == request.user

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Article.objects.all()
    filter_backends = [filters.SearchFilter]  # Add this
    search_fields = ['title', 'body']  # Fields to enable search on
    # lookup_field = 'slug'

    def get_queryset(self):
        return Article.objects.all().order_by('-date_published')

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the author
        serializer.save(author=self.request.user)
