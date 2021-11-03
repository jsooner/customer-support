from django.views.generic import TemplateView
from django.urls import path
from .views import SubjectView

urlpatterns = [
    path('create', SubjectView.as_view()),
]

