from django import template

register = template.Library()

@register.filter
def unread_notification_count(notifications):
    return notifications.unread().count()

