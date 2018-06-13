# libreria di tag da usare nei template  
# va messo nel template finale, non funziona l'eredita
# {% if request.user|has_group:"mygroup" %} 
#     <p>User belongs to my group 
# {% else %} 
#   <p>User doesn't belong to mygroup</p> 
# {% endif %}

from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
