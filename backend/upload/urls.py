from django.urls import path
from .views import FileUploadView, FileFilterView

urlpatterns = [
    path('images', FileFilterView.as_view()),
    path('images/upload', FileUploadView.as_view())
]
