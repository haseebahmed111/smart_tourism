from django import forms

from apps.home.models import City
from trip_vendor.models import TripVendorProfile, Trip


class TripVendorProfileFrom(forms.ModelForm):
    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Name of Your Company",
                "class": "form-control"
            }
        ))
    brief_info = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "About",
                "class": "form-control"
            }
        ))
    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Number",
                "class": "form-control"
            }
        ))
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address of Office",
                "class": "form-control"
            }
        ))
    policy = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Policy",
                "class": "form-control"
            }
        ))
    terms_and_condition = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Terms and Conditions",
                "class": "form-control"
            }
        ))

    picture = forms.ImageField(required=False)

    class Meta:
        model = TripVendorProfile
        fields = ('company_name', 'brief_info', 'mobile_number', 'address', 'policy', 'terms_and_condition', 'picture')


class TripForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title of This Trip",
                "class": "form-control"
            }
        ))
    trip_from = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "From City",
                "class": "form-control"
            }
        ))
    trip_to = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "To City",
                "class": "form-control"
            }
        ))
    accommodation = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    breakfast = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    lunch = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    dinner = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    guide = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    other_expenses = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    departure_info = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Departure Info/Time/Date",
                "class": "form-control"
            }
        ))

    services_included = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Services Included",
                "class": "form-control"
            }
        ))
    services_not_included = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Services Not Included",
                "class": "form-control"
            }
        ))
    trip_price_per_person = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Trip Price per Person",
                "class": "form-control"
            }
        ))
    picture = forms.ImageField(required=False)

    class Meta:
        model = Trip
        fields = (
            'title', 'trip_from', 'trip_to', 'accommodation', 'breakfast', 'lunch', 'dinner', 'guide', 'other_expenses',
            'departure_info', 'services_included', 'services_not_included','trip_price_per_person', 'picture')
