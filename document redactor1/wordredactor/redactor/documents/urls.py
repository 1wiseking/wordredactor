from django.urls import path
from .views import upload_document, edit_document  # Импортируем оба представления

urlpatterns = [
    path('upload/', upload_document, name='upload_document'),
    path('edit/<int:document_id>/', edit_document, name='edit_document'),
]
