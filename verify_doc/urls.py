from django.urls import path
from .views import VerifyDocView
urlpatterns = [
	path('verifyDoc/',VerifyDocView.as_view(), name='verify_doc'),
]