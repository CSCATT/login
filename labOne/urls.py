from django.urls import path
from labOne.views import LoginView

urlpatterns = [
	path('', LoginView.as_view()),
]