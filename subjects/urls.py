from django.views.generic import TemplateView
from django.urls import path
from .views import SubjectView, SubjectDetailView

urlpatterns = [
	path('<int:id>/', SubjectDetailView.as_view()),
    path('', SubjectView.as_view()),
]

