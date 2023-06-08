from django.urls import path
from pets.views import PetViews, PetDetailViews

urlpatterns = [
    path('pets/', PetViews.as_view()),
    path('pets/<int:pet_id>/', PetDetailViews.as_view()),
]