from django import forms
from .models import Property, PropertyStatus, PropertyType



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PropertyForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Property Title'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-4 rows-3 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Property Description'
        })
    )
    address_line_1 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Address Line 1',
        })
    )
    address_line_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Address Line 2'
        })
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'City',
        })
    )
    province_state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'State',
        })
    )
    zipcode = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Zip Code',
        })
    )
    latitude = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Latitude'
        })
    )
    longitude = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Longitude'
        })
    )
    status = forms.ModelChoiceField(
        queryset=PropertyStatus.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-1/3 px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg'
        })
    )
    type = forms.ModelChoiceField(
        queryset=PropertyType.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-1/3 px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg'
        })
    )
    price = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-4 text-gray-950 font-normal focus:outline-none focus:ring focus:ring-gray-950 rounded-lg',
            'placeholder': 'Rent / Sale Price'
        })
    )
    

    class Meta:
        model = Property
        fields = (
            'title', 'type', 'status', 'description', 'price', 'address_line_1', 'address_line_2', 'city',
            'province_state', 'zipcode', 'latitude', 'longitude'
        )
        labels = {
            'title': 'Property Title',
            'description': 'Property Description',
            'status': 'Property Status',
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City',
            'province_state': 'State',
            'zipcode': 'Postal Code',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }
        



class PropertyImageForm(forms.Form):
    images = MultipleFileField()
    class Meta:
        model = Property
        fields = ['image']




# class PropertyImageForm(forms.ModelForm):
#     image = MultipleFileField(label='Upload Images')

#     class Meta:
#         model = PropertyImage
#         fields = ['image']
#         widgets = {
#             'class': 'w-full px-4 py-4 focus:outline-none focus:ring focus:ring-gray-700 rounded-lg'
#         }
