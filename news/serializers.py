from rest_framework import serializers
from news.models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
