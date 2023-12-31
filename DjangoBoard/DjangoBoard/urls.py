from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boardApp.urls')),
    path('blogger/', include('BlogEditor.urls')),
    path('api/', include('BlogEditor.Api.urls')),
]
