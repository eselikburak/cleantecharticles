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
                                related_name="user_profile",
                                null=False, 
                                on_delete=models.CASCADE,
                                unique=True)

    user_type = models.CharField(choices=USER_TYPE,
                                 null=False, 
                                 blank=False, 
                                 default=DEFAULT_USER_TYPE, 
                                 max_length=15)

    user_image = models.ImageField(upload_to="images/accounts/", default="images/accounts/default_user_image.jpg")

    user_biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.id}: {self.user_type}"