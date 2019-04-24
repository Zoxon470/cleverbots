from django.urls import path
from .views import ImageUploadView, ImageFilterView

urlpatterns = [
    path('photos', ImageFilterView.as_view()),
    path('photo', ImageUploadView.as_view())
]
