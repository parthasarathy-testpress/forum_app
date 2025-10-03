import hashlib
from urllib.parse import urlencode
from django import template

register = template.Library()

@register.filter
def gravatar(user, size=256):
    
    if not user.email:
        return ''  # Return empty string if no email

    email = user.email.lower().encode('utf-8')
    default = 'mm'  # Default Gravatar image
    params = urlencode({'d': default, 's': str(size)})
    url = f'https://www.gravatar.com/avatar/{hashlib.md5(email).hexdigest()}?{params}'
    return url