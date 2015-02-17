
from django import forms

from marketpulse.main.models import Contribution, Location


class ContributionForm(forms.ModelForm):

    class Meta:
        model = Contribution
        fields = ['device', 'comment', 'availability']
        widgets = {'availability': forms.CheckboxInput()}


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['shop_name', 'lat', 'lng', 'link', 'country', 'is_online']
        widgets = {'lat': forms.HiddenInput(),
                   'lng': forms.HiddenInput()}

    def clean(self):
        cdata = super(LocationForm, self).clean()
        if cdata['is_online'] and not cdata['country']:
            msg = 'Please provide a country'
            self._errors['country'] = self.error_class([msg])

    def save(self, commit=True):
        """Override save method for custom functionality."""
        location = super(LocationForm, self).save(commit=False)
        # Get the location data from mapbox
        # TODO: get the actual data
        location.save()
        return location
