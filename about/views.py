from django.shortcuts import render
from .models import About
from .forms import AboutForm

# Create your views here.


# Created about_me view that renders all info of about model
def about_us(request):
    """
    Display and insert record in About model.
    """
    aboutset = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about_us.html",
        {
            "about": aboutset
        },
    )
