from django.core.cache import cache

from blog.models import Blog
from config.settings import CACHE_ENABLED


def get_posts():
    if CACHE_ENABLED:
        key = f"blogs_list"
        posts_list = cache.get(key)
        if posts_list is None:
            posts_list = Blog.objects.all()
            cache.set(posts_list, posts_list)
    else:
        posts_list = Blog.objects.all()

    return posts_list
