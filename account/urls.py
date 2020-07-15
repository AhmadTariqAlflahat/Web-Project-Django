from django.urls import path
from django.conf.urls.static import static

from web_project import settings
from account.views import (
    index, about
)

app_name = 'account'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)