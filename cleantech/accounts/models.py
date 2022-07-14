from django.db import models
from django.contrib.auth.models import User

USER_TYPE = [
    ('reader', 'reader'),
    ('blog_author', 'blog_author'),
    ('tutorial_author', 'tutorial_author')
]

DEFAULT_USER_TYPE = 'reader'

class Profile(models.Model):
    user = models.OneToOneField(User, 
                                null=True, 
                                on_delete=models.CASCADE)

    user_type = models.CharField(choices=USER_TYPE,
                                 null=True, 
                                 blank=True, 
                                 default=DEFAULT_USER_TYPE, 
                                 max_length=15)

    def __str__(self):
        return str(self.user)