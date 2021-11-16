from django import forms
from cities.models import City
from planes.models import Plane


class PlaneForm(forms.ModelForm):
    name = forms.CharField(label='Plane number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter plane number'
    }))
    travel_time = forms.IntegerField(
        label='Travel time', widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': 'Enter travel time'})
    )
    from_city = forms.ModelChoiceField(
        label='From', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    to_city = forms.ModelChoiceField(
        label='To', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Plane
        fields = '__all__'