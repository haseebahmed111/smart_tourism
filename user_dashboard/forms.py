from django import forms

from apps.home.models import City
from .models import ShareTrip, RoleElevationRequest, Complaint


class ShareTripForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Short Info",
                "class": "form-control"
            }
        ))
    from_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "From City",
                "class": "form-control"
            }
        ))
    to_city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "To City",
                "class": "form-control"
            }
        ))

    vehicle = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Vehicle you used",
                "class": "form-control"
            }
        ))
    date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ))
    trip_duration = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Number of Days Spent on this Trip",
                "class": "form-control"
            }
        ))
    persons = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Total Persons on Trip",
                "class": "form-control"
            }
        ))
    total_budget_spent = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Total Budget Spent",
                "class": "form-control"
            }
        ))
    budget_spent_food = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Budget Spent on Food",
                "class": "form-control"
            }
        ))
    budget_spent_accommodation = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Budget Spent on Hotelling",
                "class": "form-control"
            }
        ))
    budget_spent_travelling = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Budget Spent on Fuel Etc",
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Share your Trip experience",
                "class": "form-control"
            }
        ))

    image = forms.ImageField(required=False)

    class Meta:
        model = ShareTrip
        fields = ('title', 'from_city', 'to_city', 'vehicle', 'date', 'trip_duration', 'persons', 'total_budget_spent',
                  'budget_spent_food',
                  'budget_spent_accommodation', 'budget_spent_travelling', 'description', 'image')


class RoleForm(forms.ModelForm):
    role = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Requested Role",
                "class": "form-control",

            }
        ))
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Number",
                "class": "form-control"
            }
        ))
    info = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Why you need this Role?",
                "class": "form-control"
            }
        ))

    class Meta:
        model = RoleElevationRequest
        fields = ('role', 'contact_number', 'info')


class ComplaintForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Complaining for",
                "class": "form-control",

            }
        ))
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Contact Number",
                "class": "form-control"
            }
        ))
    complaint_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Please Explain issue you faced",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Complaint
        fields = ('title', 'contact_number', 'complaint_description')
