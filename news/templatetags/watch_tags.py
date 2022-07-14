from django import template

from news.models import News

register = template.Library()

@register.simple_tag()
def get_watch():

    model = News
    model.watch_users += 1
    model.save()
    return model
