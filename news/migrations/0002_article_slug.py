from django.db import migrations, models
from django.utils.text import slugify

def generate_unique_slugs(apps, schema_editor):
    Article = apps.get_model('news', 'Article')
    for article in Article.objects.all():
        base_slug = slugify(article.title)
        slug = base_slug
        counter = 1
        while Article.objects.filter(slug=slug).exclude(pk=article.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        article.slug = slug
        article.save()

class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.RunPython(generate_unique_slugs),
    ]
