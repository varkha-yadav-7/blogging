from django import template
from home.models import Posts,Users
import json

register = template.Library()

@register.simple_tag

def likers(post):
    postid=post.id
    l=Posts.objects.get(id=postid)
    like=json.loads(l.Likes)
    for i in like:
        try:
            user=Users.objects.get(Username=i)
            i=user.Username
        except:
            k=like.index(i)
            like[k]='Blogger'
    likes=json.dumps(like)
    return likes