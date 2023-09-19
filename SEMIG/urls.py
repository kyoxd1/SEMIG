from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from SEMIG.settings import base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('questionsRules.urls'))
] + static(base.STATIC_URL, document_root=base.STATIC_ROOT)
