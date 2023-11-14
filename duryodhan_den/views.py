from django.shortcuts import render
from django.http import HttpResponse

def display_image(request, pk):
    correct_answer = 92647925689224332 

    try:
        user_answer = int(pk)

        if user_answer == correct_answer:
            image_url = "https://res.cloudinary.com/dhkv5hazp/image/upload/v1699938682/node5_xghvua.png"  
            return render(request, 'photo.html', {'image_url': image_url})
        else:
            return HttpResponse("Wrong answer. Please try again.")

    except ValueError:
        return HttpResponse("Invalid input. Please enter a valid integer.")
