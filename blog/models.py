from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from markupfield.fields import MarkupField
#we define objects in the app models file. Here we define a post object.
"""
class is a special keyword that indicates that we are defining an object.
Post is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
models.Model means that the Post is a Django Model, so Django knows that it should be saved in the database.
"""

"""
    The last step here is to add our new model to our database. First we have to make Django know that we have some changes in our model. (We have just created it!) Go to your console window and type python manage.py makemigrations blog

Then: Django prepared a migration file for us that we now have to apply to our database. Type python manage.py migrate blog and the output should be as follows
    """

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = MarkupField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

    

