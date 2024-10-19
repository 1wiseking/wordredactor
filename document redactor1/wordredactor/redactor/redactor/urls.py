from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', include('documents.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from documents.views import upload_document

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', include('documents.urls')),
    path('', upload_document, name='upload_document'),  # Добавляем корневой URL
]
