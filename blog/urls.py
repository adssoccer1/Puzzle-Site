"""
    Here we're importing Django's function path and all of our views from the blog application.
    """

from django.urls import path
from . import views

"""
    As you can see, we're now assigning a view called post_list to the root URL. This URL pattern will match an empty string and the Django URL resolver will ignore the domain name (i.e., http://127.0.0.1:8000/) that prefixes the full URL path. This pattern will tell Django that views.post_list is the right place to go if someone enters your website at the 'http://127.0.0.1:8000/' address.
    """
urlpatterns = [
               path('', views.post_list, name='post_list'),
               ]
