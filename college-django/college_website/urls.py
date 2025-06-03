from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main app URLs (homepage, about, contact)
    path('', include('main.urls')),

    # Student-related URLs
    path('students/', include('students.urls')),

    # Faculty-related URLs
    path('faculty/', include('faculty.urls')),

    # Optional: Account/Auth system
    path('accounts/', include('accounts.urls')),

    # Optional: Django's built-in auth views (login/logout/password)
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
