
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), #make this pull from core login
    path('notes/', include('note_page.urls')),
    path('calendar/', include('calendar_page.urls'))
]
