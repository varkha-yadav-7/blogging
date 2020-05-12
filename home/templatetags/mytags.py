from django import template
from home.models import Posts,Users,Comments,Notifications
import json

register=template.Library()

@register.simple_tag
def getLikes(id,likes):
    if str(id) in likes:
        return 'Liked' 
    return 'Like'

@register.simple_tag
def getBookmarks(id,book):
    if str(id) in book:
        return 'Bookmarked'
    return 'Bookmark'

@register.simple_tag
def totalLikes(pid):
    p=Posts.objects.get(id=pid)
    k=json.loads(p.Likes)
    return len(k)

@register.simple_tag
def totalComments(pid):
    c=Comments.objects.filter(Post_id=pid).count()
    return c

@register.simple_tag
def totalNotifications(user):
    n=Notifications.objects.filter(Username=user,read=False).count()
    if n!=0:
        return n
    else:
        return ''