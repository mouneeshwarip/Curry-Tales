from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required
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

@login_required
def edit_about_us(request):
    """ Edit About us page of the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    about_us = get_object_or_404(About)
    if request.method == 'POST':
        about_form = AboutForm(request.POST, request.FILES, instance=about_us)
        if about_form.is_valid():
            about_form.save()
            messages.success(request, 'Successfully Updated About Us!')
            return redirect(reverse('about'))
        else:
            messages.error(
                request,
                'Failed to update About Us. Please ensure the form is valid.'
            )
    else:
        about_form = AboutForm(instance=about_us)
        messages.info(request, f'You are editing About Us')

    template = 'about/edit_about_us.html'
    context = {
        'about_form': about_form,
        'about_us': about_us,
    }

    return render(request, template, context)    
