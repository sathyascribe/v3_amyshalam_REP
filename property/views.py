from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm, PropertyImageForm
from .models import Property, PropertyStatus, PropertyImage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

# Create your views here.


# @login_required
# def create_property(request):
#   if request.method == 'POST':
#     form = PropertyForm(request.POST, request.FILES)
#     if form.is_valid():
#       form.save()  
#   # Django will automatically save the model and uploaded images
#       return redirect('property_list')
#   else:
#     form = PropertyForm()

#   return render(request, 'create_property.html', {'form': form})

# def create_property(request):
#   if request.method == 'POST':
#     property_form = PropertyForm(request.POST)
#     image_form = PropertyImageForm(request.FILES, request.POST)  # Use request.FILES for images
#     if property_form.is_valid() and image_form.is_valid():
#       # Save property data from PropertyForm
#       property = property_form.save(commit=False)  # Don't save yet
#       # Access cleaned data from PropertyForm
#       property.title = property_form.cleaned_data['title']
#       # ... (access other cleaned data as needed)

#       property.save()  # Now save the property

#       # Handle image uploads from PropertyImageForm
#       for image in image_form.cleaned_data['images']:
#         property_image = Property(property=property, image=image)
#         property_image.save()

#       # Redirect to success page or other logic
#       return redirect('property:property_list')  # Replace with your desired redirect URL
#   else:
#     property_form = PropertyForm()
#     image_form = PropertyImageForm()

#   context = {'property_form': property_form, 'image_form': image_form}
#   return render(request, 'create_property.html', context)



# def create_property(request):
#     if request.method == 'POST':
#         property_form = PropertyForm(request.POST, request.FILES)
#         if property_form.is_valid():
#             try:
#                 property = property_form.save()

#                 for image in request.FILES.getlist('images'):
#                     # Save the image directly to the Property model's `image` field
#                     property.image = image
#                     property.save()

#                 return redirect('property:property_list')
#             except Exception as e:
#                 # Handle specific exceptions or log the error
#                 if isinstance(e, ValueError):
#                     # Handle validation errors
#                     messages.error(request, "Validation error occurred.")
#                 elif isinstance(e, IOError):
#                     # Handle file I/O errors
#                     messages.error(request, "Error saving image.")
#                 else:
#                     # Log the error for debugging
#                     logger.exception("Error creating property:")

#                 return render(request, 'create_property.html', {'property_form': property_form})
#     else:
#         property_form = PropertyForm()

#     context = {'property_form': property_form}
#     return render(request, 'create_property.html', context)


# def create_property(request):
#     if request.method == 'POST':
#         property_form = PropertyForm(request.POST, request.FILES)
#         if property_form.is_valid():
#             try:
#                 property = property_form.save(commit=False)

#                 for image in request.FILES.getlist('images'):
#                     property.image = image
#                     property.save()  # Save the property for each image

#                     # Print for debugging
#                     print(f"Image saved: {image.name}")

#                 return redirect('property:property_list')
#             except Exception as e:
#                 # ... (error handling as before)
#                 return render(request, 'create_property.html', {'property_form': property_form})
#         else:
#             # ... (handle invalid form)
#             return render(request, 'create_property.html', {'property_form': property_form})
#     else:
#         # ... (handle GET request)
#         return render(request, 'create_property.html', {'property_form': PropertyForm()})

@login_required
def create_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        property_image_form = PropertyImageForm(request.POST, request.FILES)

        try:
            if property_form.is_valid() and property_image_form.is_valid():
                property = property_form.save()
                for image in request.FILES.getlist('image'):
                    image_instance = PropertyImage(property=property, image=image)
                    image_instance.save()
                return redirect('property:property_detail', property_id=property.id)
        except Exception as e:
            print(f"An error occurred: {e}") 
    else:
        property_form = PropertyForm()
        property_image_form = PropertyImageForm()

    context = {
        'property_form': property_form,
        'property_image_form': property_image_form,
    }
    return render(request, 'create_property.html', context)

@login_required
def property_list_view(request):
    try:
        available_status = PropertyStatus.objects.get(name='Available')
        properties = Property.objects.filter(status=available_status).order_by('-created_at').prefetch_related('propertyimage_set')

    except PropertyStatus.DoesNotExist:
        properties = []
        messages.error(request, "No 'available' status found in the system. Please add it first.")
    return render(request, 'property_list.html', {'properties': properties})


# @login_required
# def property_detail(request, property_id):
#     property_instance = get_object_or_404(Property, id=property_id, status__name='Available')
#     return render(request, 'property_detail.html', {'property': property_instance})

@login_required
def property_detail_view(request, property_id):
    property=get_object_or_404(Property, id=property_id)
    images = property.propertyimage_set.all()

    context = {
        'property': property,
        'images': images,
    }

    return render(request, 'property_detail.html', context)


@login_required
def property_delete_view(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.delete()
    return redirect('property:property_list')