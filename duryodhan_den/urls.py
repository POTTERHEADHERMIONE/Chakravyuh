from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.display_image, name='display_image'),
    # enter the key here to go to the next path 
]
