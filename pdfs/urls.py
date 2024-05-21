from django.urls import path
from pdfs import views

urlpatterns = [
    path("", views.upload_pdf, name="upload_pdf"),
]