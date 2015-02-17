from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render

from marketpulse.main import FFXOS_ACTIVITY_NAME, forms
from marketpulse.main.models import Activity, Contribution


def home(request):
    return render(request, 'home.html')


def activities(request):
    return redirect(reverse('main:fxosprice_new'))


@login_required
def edit_fxosprice(request, username='', id=None):
    user = request.user

    if not id:
        activity = Activity.objects.get(name=FFXOS_ACTIVITY_NAME)
        contribution = Contribution(activity=activity)
    else:
        contribution = get_object_or_404(Contribution, pk=id, user=user)

    contribution_form = forms.ContributionForm(request.POST or None, instance=contribution)
    location_form = forms.LocationForm(request.POST or None)

    if location_form.is_valid():
        import ipdb; ipdb.set_trace()  # XXX BREAKPOINT

    return render(request, 'fxosprice_new.html',
                  {'contribution_form': contribution_form,
                   'location_form': location_form,
                   'mapbox_id': settings.MAPBOX_MAP_ID,
                   'mapbox_token': settings.MAPBOX_TOKEN})


def view_fxosprice(request):
    return render(request, 'home.html')
