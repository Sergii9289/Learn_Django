from django.contrib import admin
from .models import BlogPost, Profile, Category

@admin.action(description="Додати категорію 'Новини' до вибраних постів")
def add_news_category(modeladmin, request, queryset):
    # знаходимо або створюємо категорію "Новини"
    news_category, created = Category.objects.get_or_create(name="Новини")
    for post in queryset:
        post.categories.add(news_category)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'days_since_published')
    search_fields = ('author__name', 'title')
    list_filter = ('created_at',)
    actions = [add_news_category]   # 👈 додаємо дію

    def days_since_published(self, obj):
        from datetime import date
        delta = date.today() - obj.created_at.date()
        return delta.days
    days_since_published.short_description = 'Днів з публікації'

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Profile)