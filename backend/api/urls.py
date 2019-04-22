from django.urls import path, include

urlpatterns = [
    path('upload/', include('upload.urls')),
]
