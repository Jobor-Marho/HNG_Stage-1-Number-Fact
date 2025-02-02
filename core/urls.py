"""
Url mapping settings for project
"""

from django.urls import path, include

urlpatterns = [
    path("api/", include("numbapp.urls"))
]
