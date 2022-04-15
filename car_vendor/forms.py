from django import forms

from apps.home.models import City
from car_vendor.models import CarVendorProfile, Car


class CarVendorProfileFrom(forms.ModelForm):
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
        model = CarVendorProfile
        fields = ('company_name', 'brief_info', 'mobile_number', 'address', 'policy', 'terms_and_condition', 'picture')


class CarForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title of Car",
                "class": "form-control"
            }
        ))
    make = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Make eg. Toyota",
                "class": "form-control"
            }
        ))
    model = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Model eg. Aqua",
                "class": "form-control"
            }
        ))
    year = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Year eg. 2018",
                "class": "form-control"
            }
        ))

    seating_capacity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Seating Capacity",
                "class": "form-control"
            }
        ))
    fuel_average = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Fuel Average",
                "class": "form-control"
            }
        ))
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "City",
                "class": "form-control"
            }
        ))
    driver = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-control"
            }
        ))
    rent_with_driver = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Rent with Driver",
                "class": "form-control"
            }
        ))
    rent_without_driver = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Rent without Driver",
                "class": "form-control"
            }
        ))
    picture = forms.ImageField(required=False)

    class Meta:
        model = Car
        fields = (
        'title', 'make', 'model', 'year', 'city', 'seating_capacity', 'fuel_average', 'driver', 'rent_with_driver',
        'rent_without_driver', 'picture')
