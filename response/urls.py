from django.urls import path, include
from .views import ReponseView

urlpatterns = [
	path('', include('djoser.urls')),
	path('', include('djoser.urls.authtoken')),
    path('list', ReponseView.as_view()),
]

