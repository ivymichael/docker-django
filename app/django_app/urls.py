from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("frontend.urls")),
    path("", include("leads.urls")),
    path("", include('accounts.urls')),
    path("upload/", include("upload.urls")),
    path('admin/', admin.site.urls),
]

if bool(settings.DEBUG):
    print(settings.DEBUG)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
