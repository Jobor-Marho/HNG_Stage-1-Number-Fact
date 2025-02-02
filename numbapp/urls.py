"""
Urls mappings for numbapp
"""

from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path("classify-number", views.analyzeNum, name="analyze-num")
]