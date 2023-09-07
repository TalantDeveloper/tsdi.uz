from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = i18n_patterns(
    path('', include('main.urls')),  # Main app urls
    path('faculty/', include('faculty.urls')),  # Faculty app urls
    path('page/', include('page.urls')),  # Page app urls
    path('new/', include('new.urls')),  # New app urls
    path('admin/', admin.site.urls),  # Admin panels urls
    path('uploads', include('ckeditor_uploader.urls')),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Static urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Media urls
