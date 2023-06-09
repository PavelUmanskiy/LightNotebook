from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Light_Notebook.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]  + static(MEDIA_URL, document_root=MEDIA_ROOT)
