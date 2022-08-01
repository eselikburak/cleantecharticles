from django.db import models

class Home(models.Model):
    header_title = models.CharField(max_length=200, 
                                    null=True, 
                                    blank=True, 
                                    verbose_name='Header Section Title')
    header_description = models.TextField(null=True, 
                                          blank=True,
                                          verbose_name='Header Section Description')

    tut1_title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tutorial 1 Title')
    tut1_description = models.TextField(null=True, blank=True, verbose_name='Tutorial 1 Description')

    tut2_title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tutorial 2 Title')
    tut2_description = models.TextField(null=True, blank=True, verbose_name='Tutorial 2 Description')

    middle_section_title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Middle Section Title')
    middle_section_description = models.TextField(null=True, blank=True, verbose_name='Middle Section Description')
    middle_section_img = models.ImageField(null=True, blank=True, upload_to='images/')

    tut3_title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tutorial 3 Title')
    tut3_description = models.TextField(null=True, blank=True, verbose_name='Tutorial 3 Description')

    tut4_title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tutorial 4 Title')
    tut4_description = models.TextField(null=True, blank=True, verbose_name='Tutorial 4 Description')

    social_sec_title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Social Section Title')
    social_sec_description = models.TextField(null=True, blank=True, verbose_name='Social Section Description')


    instagram_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Instagram Url')
    twitter_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Twitter Url')
    github_url = models.URLField(max_length=200,null=True, blank=True, verbose_name='Github Url')

    def __str__(self) -> str:
        return f'Home Object - {self.header_title}'

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=100, verbose_name="Email")
    subject = models.CharField(max_length=150, null=True, verbose_name="Subject")
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email