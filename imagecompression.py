from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image


def compress_image(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        uploaded_file = request.FILES['image']

        # Open the uploaded image using PIL
        image = Image.open(uploaded_file)

        # Perform image compression
        max_image_size = 1024  # Maximum width or height in pixels
        aspect_ratio = image.width / image.height
        new_width = int(max_image_size * aspect_ratio)
        new_height = max_image_size
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create a response object with the compressed image
        response = HttpResponse(content_type='image/png')
        resized_image.save(response, 'PNG')

        # Set the appropriate headers for file download
        response['Content-Disposition'] = 'attachment; filename="compressed_image.png"'

        return response

    return render(request, 'imagecompression/upload.html')
