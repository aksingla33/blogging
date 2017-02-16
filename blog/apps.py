from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    from .models import Post

admin.site.register(Post)
