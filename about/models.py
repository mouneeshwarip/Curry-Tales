from django.db import models


# Create About model
class About(models.Model):
    """
    Stores single about us request.
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"